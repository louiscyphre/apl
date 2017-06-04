# -*- coding: utf-8 -*-
#
# lab is a Python API for running and evaluating algorithms.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Main module for creating experiments."""

from collections import OrderedDict
import logging
import os
import pkgutil
import sys

from lab import environments
from lab import tools
from lab.fetcher import Fetcher
from lab.steps import Step, get_step, get_steps_text


# How many tasks to group into one top-level directory.
SHARD_SIZE = 100

# Make argparser available globally so users can add custom arguments.
ARGPARSER = tools.get_parser()
ARGPARSER.epilog = "The list of available steps will be added later."
steps_group = ARGPARSER.add_mutually_exclusive_group()
steps_group.add_argument(
    'steps', metavar='step', nargs='*', default=[],
    help='Name or number of a step below. If none is given, print help.')
steps_group.add_argument(
    '--all', dest='run_all_steps', action='store_true',
    help='Run all steps.')


def get_default_data_dir():
    """E.g. "ham/spam/eggs.py" => "ham/spam/data/"."""
    return os.path.join(os.path.dirname(tools.get_script_path()), "data")


def _get_default_experiment_name():
    """Get default name for experiment.

    Derived from the filename of the main script, e.g.
    "ham/spam/eggs.py" => "eggs".
    """
    return os.path.splitext(os.path.basename(tools.get_script_path()))[0]


def _get_default_experiment_dir():
    """E.g. "ham/spam/eggs.py" => "ham/spam/data/eggs"."""
    return os.path.join(
        get_default_data_dir(), _get_default_experiment_name())


def get_run_dir(task_id):
    lower = ((task_id - 1) / SHARD_SIZE) * SHARD_SIZE + 1
    upper = ((task_id + SHARD_SIZE - 1) / SHARD_SIZE) * SHARD_SIZE
    return "runs-{lower:0>5}-{upper:0>5}/{task_id:0>5}".format(**locals())


class _Buildable(object):
    """Abstract base class for Experiment and Run."""
    def __init__(self):
        self.resources = []
        self.new_files = []
        self.env_vars_relative = {}
        self.commands = OrderedDict()
        self.properties = tools.Properties()

    def set_property(self, name, value):
        """Add a key-value property.

        These can be used later, for example, in reports. ::

            exp.set_property('suite', ['gripper', 'grid'])

            run.set_property('domain', 'gripper')
            run.set_property('problem', 'prob01.pddl')

        Each run must have the property *id* which must be a *unique*
        list of strings. They determine where the results for this run
        will land in the combined properties file. ::

            run.set_property('id', [algorithm, benchmark])
            run.set_property('id', [algorithm, domain, problem])

        """
        self.properties[name] = value

    def _check_alias(self, name):
        if name and not (name[0].isalpha() and name.replace('_', '').isalnum()):
            logging.critical(
                'Resource names must start with a letter and consist '
                'exclusively of letters, numbers and underscores: {}'.format(name))
        if name in self.env_vars_relative:
            logging.critical('Resource names must be unique: {!r}'.format(name))

    def add_resource(self, name, source, dest='', required=True, symlink=False):
        """Include the file or directory *source* in the experiment or run.

        *name* is an alias for the resource in commands. It must start with a
        letter and consist exclusively of letters, numbers and underscores.
        If you don't need an alias for the resource, set name=''.

        *source* is copied to /path/to/exp-or-run/*dest*. If *dest* is
        omitted, the last part of the path to *source* will be taken as the
        destination filename. If you only want an alias for your resource, but
        don't want to copy or link it, set *dest* to None.

        Example::

            exp.add_resource('planner', 'path/to/my-planner', dest='planner')

        includes my-planner in the experiment directory. You can use
        ``{planner}`` to reference my-planner in a run's commands::

            run.add_resource('domain', 'path-to/gripper/domain.pddl')
            run.add_resource('problem', 'path-to/gripper/prob01.pddl')
            run.add_command('solve', ['{planner}', '{domain}', '{problem}'])

        """
        if dest == '':
            dest = os.path.basename(source)
        if dest is None:
            dest = os.path.abspath(source)
        self._check_alias(name)
        if name:
            self.env_vars_relative[name] = dest
        self.resources.append((source, dest, required, symlink))

    def add_new_file(self, name, dest, content, permissions=0o644):
        """
        Write *content* to /path/to/exp-or-run/*dest* and make the new file
        available to the commands as *name*.

        *name* is an alias for the resource in commands. It must start with a
        letter and consist exclusively of letters, numbers and underscores. ::

            run.add_new_file('learn', 'learn.txt', 'a = 5; b = 2; c = 5')
            run.add_command('print-trainingset', ['cat', '{learn}'])

        """
        self._check_alias(name)
        if name:
            self.env_vars_relative[name] = dest
        self.new_files.append((dest, content, permissions))

    def add_command(self, name, command, time_limit=None, memory_limit=None, **kwargs):
        """Call an executable.

        If invoked on a *run*, this method adds the command to the
        **specific** run. If invoked on the experiment, the command is
        appended to the list of commands of **all** runs.

        *name* is a string describing the command.

        *command* has to be a list of strings where the first item is
        the executable.

        The command is aborted after *time_limit* seconds or when it
        uses more than *memory_limit* MiB. By default no limits are
        enforced.

        All *kwargs* are passed to `subprocess.Popen
        <http://docs.python.org/library/subprocess.html>`_. Instead of
        file handles you can also pass filenames for the ``stdin``,
        ``stdout`` and ``stderr`` keyword arguments.

        Examples::

            # Add command to a *specific* run.
            run.add_command('list-directory', ['ls', '-al'])
            run.add_command(
                'solver', [path-to-solver, 'input-file'], time_limit=60)
            run.add_command(
                'preprocess', ['preprocessor-path'], stdin='output.sas')

            # Add parser to *all* runs.
            exp.add_command('parser', ['path-to-my-parser'])

        """
        if not isinstance(name, basestring):
            logging.critical('name %s is not a string' % name)
        if not isinstance(command, (list, tuple)):
            logging.critical('%s is not a list' % command)
        if not command:
            logging.critical('command "%s" cannot be empty' % name)
        if '"' in name:
            logging.critical(
                'command name mustn\'t contain double-quotes: {}'.format(name))
        if name in self.commands:
            logging.critical('a command named "%s" has already been added' % name)
        kwargs['time_limit'] = time_limit
        kwargs['memory_limit'] = memory_limit
        self.commands[name] = (command, kwargs)

    @property
    def _env_vars(self):
        return dict(
            (name, self._get_abs_path(dest))
            for name, dest in self.env_vars_relative.items())

    def _get_abs_path(self, rel_path):
        """Return absolute path by applying rel_path to the base dir."""
        return os.path.join(self.path, rel_path)

    def _get_rel_path(self, abs_path):
        return os.path.relpath(abs_path, start=self.path)

    def _build_properties_file(self):
        combined_props = tools.Properties(self._get_abs_path('properties'))
        combined_props.update(self.properties)
        combined_props.write()

    def _build_resources(self):
        for dest, content, permissions in self.new_files:
            filename = self._get_abs_path(dest)
            tools.makedirs(os.path.dirname(filename))
            logging.debug('Writing file "%s"' % filename)
            tools.write_file(filename, content)
            os.chmod(filename, permissions)

        for source, dest, required, symlink in self.resources:
            if required and not os.path.exists(source):
                logging.critical('Required resource not found: %s' % source)
            dest = self._get_abs_path(dest)
            if not dest.startswith(self.path):
                # Only copy resources that reside in the experiment/run dir.
                continue
            if symlink:
                # Do not create a symlink if the file doesn't exist.
                if not os.path.exists(source):
                    continue
                source = self._get_rel_path(source)
                os.symlink(source, dest)
                logging.debug('Linking from %s to %s' % (source, dest))
                continue

            # Even if the directory containing a resource has already been added,
            # we copy the resource since we might want to overwrite it.
            logging.debug('Copying %s to %s' % (source, dest))
            tools.copy(source, dest, required)


class Experiment(_Buildable):
    """Base class for lab experiments.

    An **experiment** consists of multiple **runs**. Each run consists
    of multiple **commands**.

    Here is a simple example:

    >>> exp = Experiment()
    >>> run = exp.add_run()
    >>> run.add_command('greet', ['echo', 'hello world'])
    >>> run.set_property('id', ['1'])  # Runs need unique IDs.

    An **experiment** also has multiple **steps**. By default the
    following ones are present:

    * Build the experiment.
    * Execute all runs.
    * Fetch the results.

    You can add report steps with :meth:`.add_report`.

    You can start an experiment's steps by calling ::

        exp.run_steps()

    This will parse the commandline and execute the selected steps.

    """
    def __init__(self, path=None, environment=None):
        """
        The experiment will be built at *path*. It defaults to
        ``<scriptdir>/data/<scriptname>/``. E.g., for the script
        ``experiments/myexp.py``, the default *path* will be
        ``experiments/data/myexp/``.

        *environment* must be an :ref:`Environment <environments>`
        instance. You can use
        :class:`~lab.environments.LocalEnvironment` to run your
        experiment on a single computer (default). If you have access
        to the computer grids in Basel or Freiburg you can use the
        predefined grid environments
        :class:`~lab.environments.MaiaEnvironment` or
        :class:`~lab.environments.GkiGridEnvironment`. Alternatively,
        you can write your own :ref:`Environment <environments>` class.

        """
        _Buildable.__init__(self)
        path = path or _get_default_experiment_dir()
        self.path = os.path.abspath(path)
        if any(char in self.path for char in (':', ',')):
            logging.critical('Path contains commas or colons: %s' % self.path)
        self.environment = environment or environments.LocalEnvironment()
        self.environment.exp = self

        self.runs = []

        self.set_property('experiment_file', self._script)

        self.add_new_file(
            "lab_default_parser",
            "lab-default-parser.py",
            pkgutil.get_data('lab', 'data/default-parser.py'),
            permissions=0o755)
        self.add_command(
            "run-lab-default-parser", [sys.executable, "{lab_default_parser}"])

        self.steps = []
        self.add_step('build', self.build)
        self.add_step('run', self.start_runs)
        self.add_fetcher(name='fetch')

    @property
    def name(self):
        """Return the directory name of the experiment's ``path``."""
        return os.path.basename(self.path)

    @property
    def eval_dir(self):
        """Return the name of the default evaluation directory.

        This is the directory where the fetched and parsed results will land by
        default.

        """
        return self.path + '-eval'

    @property
    def _script(self):
        """Return the filename of the experiment script."""
        return os.path.basename(sys.argv[0])

    def add_step(self, name, function=None, *args, **kwargs):
        """Add a step to the list of experiment steps.

        Use this method to add **custom** experiment steps like
        removing directories and publishing results. To add fetch and
        report steps, use the convenience methods ``add_fetcher()`` and
        ``add_report()``.

        *name* is a descriptive name for the step.

        *function* must be a callable Python object, e.g., a function
        or a class implementing `__call__`. We allow function to be
        None only for backwards compatibility.

        *args* and *kwargs* will be passed to the *function* when the
        step is executed.

        >>> import shutil
        >>> import subprocess
        >>> from lab.experiment import Experiment
        >>> exp = Experiment('/tmp/myexp')
        >>> exp.add_step('rm-eval-dir', shutil.rmtree, exp.eval_dir)
        >>> exp.add_step('greet', subprocess.call, ['echo', 'Hello'])

        """
        # Backwards compatibility.
        if isinstance(name, Step):
            tools.show_deprecation_warning(
                'Passing a Step object to add_step() has been deprecated. '
                'Please see the documentation of add_step().')
            if function or args or kwargs:
                raise ValueError(
                    'When passing a Step object to add_step(), no other '
                    'parameters must be given.')
            self.steps.append(name)
        else:
            self.steps.append(Step(name, function, *args, **kwargs))

    def add_fetcher(self, src=None, dest=None, name=None, filter=None,
                    parsers=None, **kwargs):
        """
        Add a step that fetches results from experiment or evaluation
        directories into a new or existing evaluation directory.

        You can use this method to combine results from multiple
        experiments.

        *src* can be an experiment or evaluation directory. It defaults
        to ``exp.path``.

        *dest* must be a new or existing evaluation directory. It
        defaults to ``exp.eval_dir``. If *dest* already contains
        data, the old and new data will be merged, not replaced.

        If no *name* is given, call this step "fetch-``basename(src)``".

        You can fetch only a subset of runs (e.g., runs for specific
        domains or algorithms) by passing :py:class:`filters <.Report>`
        with the *filter* argument.

        *parsers* can be a list of paths to parser scripts. If given,
        each parser is called in each run directory and the results are
        added to the properties file which is fetched afterwards. This
        option is useful if you forgot to parse some attributes during
        the experiment.

        Example setup:

        >>> exp = Experiment('/tmp/exp')

        Fetch all results and write a single combined properties file
        to the default evaluation directory (this step is added by
        default):

        >>> exp.add_fetcher(name='fetch')

        Merge the results from "other-exp" into this experiment's
        results:

        >>> exp.add_fetcher(src='/path/to/other-exp-eval')

        Fetch only the runs for certain algorithms:

        >>> exp.add_fetcher(filter_algorithm=['algo_1', 'algo_5'])

        Parse additional attributes:

        >>> exp.add_fetcher(parsers=['path/to/myparser.py'])

        """
        src = src or self.path
        dest = dest or self.eval_dir
        name = name or 'fetch-%s' % os.path.basename(src)
        self.add_step(
            name, Fetcher(), src, dest, filter=filter, parsers=parsers, **kwargs)

    def add_report(self, report, name='', eval_dir='', outfile=''):
        """Add *report* to the list of experiment steps.

        This method is a shortcut for ``add_step(name, report,
        eval_dir, outfile)`` and uses sensible defaults for omitted
        arguments.

        If no *name* is given, use *outfile* or the *report*'s class name.

        By default, use the experiment's standard *eval_dir*.

        If *outfile* is omitted, compose a filename from *name* and the
        *report*'s format. If *outfile* is a relative path, put it under
        *eval_dir*.

        >>> from downward.reports.absolute import AbsoluteReport
        >>> exp = Experiment("/tmp/exp")
        >>> exp.add_report(AbsoluteReport(attributes=["coverage"]))

        """
        name = name or os.path.basename(outfile) or report.__class__.__name__.lower()
        eval_dir = eval_dir or self.eval_dir
        outfile = outfile or '%s.%s' % (name, report.output_format)
        if not os.path.isabs(outfile):
            outfile = os.path.join(eval_dir, outfile)
        self.add_step(name, report, eval_dir, outfile)

    def add_run(self, run=None):
        """Schedule *run* to be part of the experiment.

        If *run* is None, create a new run, add it to the experiment
        and return it.

        """
        run = run or Run(self)
        self.runs.append(run)
        return run

    def run_steps(self):
        """Parse the commandline and run selected steps."""
        ARGPARSER.epilog = get_steps_text(self.steps)
        self.args = ARGPARSER.parse_args()
        if not self.args.steps and not self.args.run_all_steps:
            ARGPARSER.print_help()
            sys.exit(0)
        # If no steps were given on the commandline, run all exp steps.
        steps = [get_step(self.steps, name) for name in self.args.steps] or self.steps
        # Use LocalEnvironment if the main experiment step is inactive.
        if (self.args.run_all_steps or
                any(environments.is_run_step(step) for step in steps)):
            env = self.environment
        else:
            env = environments.LocalEnvironment()
        env.run_steps(steps)

    @tools.deprecated(
        "Using exp() has been deprecated in lab 2.0, please use "
        "exp.run_steps() instead.")
    def __call__(self):
        return self.run_steps()

    def _remove_experiment_dir(self):
        if os.path.exists(self.path):
            tools.confirm_overwrite_or_abort(self.path)
            tools.remove_path(self.path)

    def build(self, write_to_disk=True):
        """
        Finalize the internal data structures, then write all files
        needed for the experiment to disk.

        If *write_to_disk* is False, only compute the internal data
        structures. This is only needed internally for
        FastDownwardExperiments on grids, where build() turns the added
        algorithms and benchmarks into Runs.

        By default, the first experiment step calls this method.

        """
        if not write_to_disk:
            return

        logging.info('Experiment path: "%s"' % self.path)
        self._remove_experiment_dir()
        tools.makedirs(self.path)
        self.environment.write_main_script()

        self._build_resources()
        self._build_runs()
        self._build_properties_file()

    def start_runs(self):
        """Execute all runs that were added to the experiment.

        Depending on the selected environment this method will start
        the runs locally or on a computer cluster.

        By default, the second experiment step calls this method.

        """
        self.environment.start_runs()

    def _build_runs(self):
        """
        Uses the relative directory information and writes all runs to disc.
        """
        if not self.runs:
            logging.critical('No runs have been added to the experiment.')
        num_runs = len(self.runs)
        self.set_property('runs', num_runs)
        logging.info('Building %d runs' % num_runs)
        for index, run in enumerate(self.runs, 1):
            if index % 100 == 0:
                logging.info('Build run %6d/%d' % (index, num_runs))
            for name, (command, kwargs) in self.commands.items():
                run.add_command(name, command, **kwargs)
            run.build(index)
        logging.info('Finished building runs')


class Run(_Buildable):
    """
    An experiment consists of multiple runs. There should be one run
    for each (algorithm, benchmark) pair.

    A run consists of one or more commands.
    """
    def __init__(self, experiment):
        """
        *experiment* is a lab :py:class:`Experiment
        <lab.experiment.Experiment>` object.
        """
        _Buildable.__init__(self)
        self.experiment = experiment
        self.path = None

    def build(self, run_id):
        """Write the run's files to disk.

        This method is called automatically by the experiment.

        """
        rel_run_dir = get_run_dir(run_id)
        self.set_property('run_dir', rel_run_dir)
        self.path = os.path.join(self.experiment.path, rel_run_dir)
        os.makedirs(self.path)

        # We need to build the run script before the resources, because
        # the run script is added as a resource.
        self._build_run_script()
        self._build_resources()
        self._check_id()
        self._build_properties_file()

    def _build_run_script(self):
        if not self.commands:
            logging.critical('Please add at least one command')

        exp_vars = self.experiment._env_vars
        run_vars = self._env_vars
        doubly_used_vars = set(exp_vars) & set(run_vars)
        if doubly_used_vars:
            logging.critical(
                'Resource names cannot be shared between experiments '
                'and runs, they must be unique: {}'.format(doubly_used_vars))
        env_vars = exp_vars
        env_vars.update(run_vars)
        env_vars = self._prepare_env_vars(env_vars)

        run_script = pkgutil.get_data('lab', 'data/run-template.py')

        def make_call(name, cmd, kwargs):
            kwargs['name'] = name

            # Support running globally installed binaries.
            def format_arg(arg):
                if isinstance(arg, basestring):
                    try:
                        return repr(arg.format(**env_vars))
                    except KeyError as err:
                        logging.critical('Resource {} is undefined.'.format(err))
                else:
                    return repr(str(arg))

            def format_key_value_pair(key, val):
                if isinstance(val, basestring):
                    formatted_value = format_arg(val)
                else:
                    formatted_value = repr(val)
                return '{}={}'.format(key, formatted_value)

            cmd_string = '[{}]'.format(', '.join([format_arg(arg) for arg in cmd]))
            kwargs_string = ', '.join(format_key_value_pair(key, value)
                                      for key, value in sorted(kwargs.items()))
            parts = [cmd_string]
            if kwargs_string:
                parts.append(kwargs_string)
            call = ('retcode = Call({}, **redirects).wait()\n'
                    'save_returncode({name!r}, retcode)\n'.format(
                        ', '.join(parts), **locals()))
            return call

        calls_text = '\n'.join(
            make_call(name, cmd, kwargs)
            for name, (cmd, kwargs) in self.commands.items())

        for old, new in [('CALLS', calls_text)]:
            run_script = run_script.replace('"""%s"""' % old, new)

        self.add_new_file('', 'run', run_script, permissions=0o755)

    def _prepare_env_vars(self, env_vars):
        """Use relative filenames for paths in the experiment dir."""
        new_env_vars = {}
        for var, path in env_vars.items():
            abspath = self._get_abs_path(path)
            if abspath.startswith(self.experiment.path):
                new_env_vars[var] = self._get_rel_path(path)
            else:
                new_env_vars[var] = abspath
        return new_env_vars

    def _check_id(self):
        run_id = self.properties.get('id')
        if run_id is None:
            logging.critical('Each run must have an id')
        if not isinstance(run_id, (list, tuple)):
            logging.critical('id must be a list: {}'.format(run_id))
        for id_part in run_id:
            if not isinstance(id_part, basestring):
                logging.critical('run IDs must be a list of strings: {}'.format(run_id))

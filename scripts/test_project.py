#! /usr/bin/env python

"""Testing script to choose between best configuration."""

import os
import os.path
import platform

from lab.environments import LocalEnvironment, MaiaEnvironment

from downward.experiment import FastDownwardExperiment
from downward.reports.absolute import AbsoluteReport
from downward.reports.scatter import ScatterPlotReport


ATTRIBUTES = ['coverage', 'evaluations', 'evaluations', 'plan', 'times',
    'expansions', 'trivially_unsolvable']

if 'cluster' in platform.node():
    # Create bigger suites with suites.py from the downward-benchmarks repo.
    SUITE = ['depot', 'freecell', 'gripper', 'zenotravel']
    ENV = MaiaEnvironment(priority=0)
else:
    # TODO add suites
    SUITE = ['gripper']
    #SUITE = ['depot:p01.pddl', 'gripper:prob01.pddl']
    ENV = LocalEnvironment(processes=2)
# Change to path to your Fast Downward repository.
REPO = os.environ["DOWNWARD_REPO"]
BENCHMARKS_DIR = os.environ["DOWNWARD_BENCHMARKS"]
REVISION_CACHE = os.path.expanduser('~/lab/revision-cache')
#exp.add_resource('fast-downward', 'fast-downward.py')

exp = FastDownwardExperiment(environment=ENV, revision_cache=REVISION_CACHE)

# TODO
#run.add_command('run-planner',
#    ['fast-downward', '-o', '{domain}', '-f', '{problem}'],
#    time_limit=1800,memory_limit=2048)

exp.add_suite(BENCHMARKS_DIR, SUITE)

# TODO
exp.add_algorithm('iter-hadd', REPO, REV, ['--heuristic', 'hadd=add()',
    '--search',
    'iterated([lazy_greedy([hadd]),lazy_wastar([hadd])],repeat_last=true)'])
exp.add_algorithm('ipdb', REPO, REV, ["--search", "astar(ipdb())"],
    driver_options=['--search-time-limit', 10])
exp.add_algorithm('lama11', REPO, REV, [],
    driver_options=['--alias', 'seq-sat-lama-2011',
                        '--plan-file', 'sas_plan'])
exp.add_algorithm('sat-fdss-1', REPO, REV, [],
    driver_options=['--alias', 'seq-sat-fdss-1'])
exp.add_algorithm('opt-fdss-1', REPO, REV, [], driver_options=[
    '--portfolio',os.path.join(REPO, 'driver','portfolios',
    'seq_opt_fdss_1.py')])


##or task in suites.build_suite(BENCHMARKS_DIR, SUITE):
#    run = exp.add_run()
#    # Create symbolic links and aliases. This is optional. We
#    # could also use absolute paths in add_command().
#    run.add_resource('domain', task.domain_file, symlink=True)
#    run.add_resource('problem', task.problem_file, symlink=True)
#    # 'ff' binary has to be on the PATH.
#    # We could also use exp.add_resource().
#    run.add_command('run-planner',
#        ['ff', '-o', '{domain}', '-f', '{problem}'],
#        time_limit=1800, memory_limit=2048)
#
#    # AbsoluteReport needs the following properties:
#    # 'domain', 'problem', 'algorithm', 'coverage'.
#    run.set_property('domain', task.domain)
#    run.set_property('problem', task.problem)
#    run.set_property('algorithm', 'ff')
#    # Every run has to have a unique id in the form of a
#    # list.
#    # The algorithm name is only really needed when
#    # there are
#    # multiple algorithms.
#    run.set_property('id', ['ff', task.domain, task.problem])
#    # Schedule parser.
#    run.add_command('parse', ['{parser}'])
# Make a report (AbsoluteReport is the standard report).

exp.add_report(
    AbsoluteReport(attributes=ATTRIBUTES), outfile='report.html')

# Compare the number of expansions in a scatter plot.
exp.add_report(
    ScatterPlotReport(
        attributes=["expansions"], filter_algorithm=["blind", "lmcut"]),
    outfile='scatterplot.png')

# Parse the commandline and show or run experiment steps.
exp.run_steps()

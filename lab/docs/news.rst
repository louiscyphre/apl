News
====

.. module :: lab.experiment
.. module :: downward.experiments


v2.0 (2017-01-09)
-----------------

lab
^^^
* Show warning and ask for action when evaluation dir already exists.
* Add ``scale`` parameter to Attribute. It is used by the plot reports.
* Add ``digits`` parameter to Attribute for specifying the number of digits after the decimal point.
* Pass name, function, args and kwargs to ``exp.add_step()``. Deprecate passing Step objects.
* After calling ``add_resource("mynick", ...)``, use resource in commands with "{mynick}".
* Call: make ``name`` parameter mandatory, rename ``mem_limit`` kwarg to ``memory_limit``.
* Store grid job files in ``<exp-dir>-grid-steps``.
* Use common ``run-dispatcher`` script for local and remote experiments.
* LocalEnvironment: support randomizing task order (enabled by default).
* Make ``path`` parameter optional for all experiments.
* Warn if steps are listed explicitly and ``--all`` is used.
* Change main experiment step name from "start" to "run".
* Deprecate ``exp()``. Use ``exp.run_steps()`` instead.
* Don't filter ``None`` values in ``lab.reports`` helper functions.
* Make logging clearer.
* Add example FF experiment.
* Remove deprecated code (e.g. predefined Step objects, ``tools.sendmail()``).
* Remove ``Run.require_resource()``. All resources have always been available for all runs.
* Fetcher: remove ``write_combined_props`` parameter.
* Remove ``Sequence`` class.
* Parser: remove ``key_value_patterns`` parameter. A better solution is in the works.
* Remove ``tools.overwrite_dir()`` and ``tools.get_command_output()``.
* Remove ``lab.reports.minimum()``, ``lab.reports.maximum()``, ``lab.reports.stddev()``.
* Move ``lab.reports.prod()`` to ``lab.tools.product()``.
* Rename ``lab.reports.gm()`` to ``lab.reports.geometric_mean()`` and
  ``lab.reports.avg()`` to ``lab.reports.arithmetic_mean()``.
* Many speed improvements and better error messages.
* Rewrite docs.

downward
^^^^^^^^
* Always validate plans. Previous lab versions don't add ``--validate``
  since older Fast Downward versions don't support it.
* HTML reports: hide tables by default, add buttons for toggling visibility.
* Unify "score_*", "quality" and "coverage" attributes: assign values in range [0, 1]
  and compute only sum and no average.
* Don't print tables on commandline.
* Remove DownwardExperiment and other deprecated code.
* Move ``FastDownwardExperiment`` into ``downward/experiment.py``.
* Rename ``config`` attribute to ``algorithm``. Remove ``config_nick`` attribute.
* Change call name from "search" to "fast-downward".
* Remove "memory_capped", and "id_string" attributes.
* Report raw memory in "unexplained errors" table.
* Parser: remove ``group`` argument from ``add_pattern()``, and always use group 1.
* Remove ``cache_dir`` parameter. Add ``revision_cache`` parameter to ``FastDownwardExperiment``.
* Fetcher: remove ``copy_all`` option.
* Remove predefined benchmark suites.
* Remove IpcReport, ProblemPlotReport, RelativeReport, SuiteReport and TimeoutReport.
* Rename CompareConfigsReport to ComparativeReport.
* Remove possibility to add ``_relative`` to an attribute to obtain relative results.
* Apply filters sequentially instead of interleaved.
* PlanningReport: remove ``derived_properties`` parameter. Use two filters
  instead: one for caching results, the other for adding new properties
  (see ``QualityFilters`` in ``downward/reports/__init__.py``).
* PlotReport: use fixed legend location, remove ``category_styles`` option.
* AbsoluteReport: remove ``colored`` parameter and always color HTML reports.
* Don't use domain links in Latex reports.
* AbsoluteReport: Remove ``resolution`` parameter and always use ``combined`` resolution.
* Rewrite docs.


v1.12 (2017-01-09)
------------------

downward
^^^^^^^^
* Only compress "output" file if it exists.
* Preprocess parser: make legacy preprocessor output optional.


v1.11 (2016-12-15)
------------------

lab
^^^
* Add bitbucket-pipelines.yml for continuous integration testing.

downward
^^^^^^^^
* Add IPC 2014 benchmark suites (Silvan).
* Set ``min_wins=False`` for ``dead_ends`` attribute.
* Fit coordinates better into plots.
* Add finite_sum() function and use it for ``initial_h_value`` (Silvan).
* Update example scripts for repos without benchmarks.
* Update docs.


v1.10 (2015-12-11)
------------------

lab
^^^
* Add ``permissions`` parameter to :func:`Experiment.add_new_file()`.
* Add default parser which checks that log files are not bigger than 100 MB. Maybe we'll make this configurable in the future.
* Ensure that resource names are not shared between runs and experiment.
* Show error message if resource names are not unique.
* Table: don't format list items. This allows us to keep the quotes for configuration lists.

downward
^^^^^^^^
* Cleanup :py:mod:`downward.suites`: update suite names, add STRIPS and
  ADL versions of all IPCs. We recommend selecting a subset of domains
  manually to only run your code on "interesting" benchmarks. As a
  starting point you can use the suites ``suite_optimal_strips`` or
  ``suite_satisficing``.


v1.9.1 (2015-11-12)
-------------------

downward
^^^^^^^^
* Always prepend build options with ``-j<num_cpus>``.
* Fix: Use correct revisions in ``FastDownwardExperiment``.
* Don't abort parser if resource limits can't be found (support old planner versions).


v1.9 (2015-11-07)
-----------------

lab
^^^
* Add :func:`lab.experiment.Experiment.add_command()` method.
* Add :py:data:`lab.__version__` string.
* Explicitly remove support for Python 2.6.

downward
^^^^^^^^
* Add :py:class:`downward.experiment.FastDownwardExperiment` class for whole-planner experiments.
* Deprecate :py:class:`downward.experiments.DownwardExperiment` class.
* Repeat headers between domains in :py:class:`downward.reports.taskwise.TaskwiseReport`.


v1.8 (2015-10-02)
-----------------

lab
^^^
* Deprecate predefined experiment steps (``remove_exp_dir``,
  ``zip_exp_dir``, ``unzip_exp_dir``).
* Docs: add FAQs, update docs.
* Add more regression and style tests.

downward
^^^^^^^^
* Parse both evaluated states (evaluated) and evaluations (evaluations).
* Add example experiment showing how to make reports for data obtained without lab.
* Add suite_sat_strips().
* Parse negative initial h values.
* Support CMake builds.


v1.7 (2015-08-19)
-----------------

lab
^^^
* Automatically determine whether to queue steps sequentially on the grid.
* Reports: right-align headers (except the left-most one).
* Reports: let :func:`lab.reports.gm` return 0 if any of the numbers is 0.
* Add test that checks for dead code with vulture.
* Remove Step.remove_exp_dir step.
* Remove default time and memory limits for commands. You can now pass
  ``mem_limit=None`` and ``time_limit=None`` to disable limits for a
  command.
* Pass ``extra_options`` kwarg to
  :py:class:`lab.environments.OracleGridEngineEnvironment` to set
  additional options like parallel environments.
* Sort ``properties`` files by keys.

downward
^^^^^^^^
* Add support for new python driver script ``fast-downward.py``.
* Use booktabs package for latex tables.
* Remove vertical lines from Latex tables (recommended by booktabs docs).
* Capitalize attribute names and remove underscores for Latex reports.
* Allow fractional plan costs.
* Set search_time and total_time to 0.01 instead of 0.1 if they are 0.0 in the log.
* Parse initial h-value for aborted searches (Florian).
* Use EXIT_UNSOLVABLE instead of logs to determine unsolvability.
  Currently, this exit code is only returned by EHC.
* Exit with warning if search parser is not executable.
* Deprecate ``downward/configs.py`` module.
* Deprecate ``examples/standard_exp.py`` module.
* Remove ``preprocess-all.py`` script.
* By default, use all CPUs for compiling Fast Downward.


v1.6
----

lab
^^^
* Restore earlier default behavior for grid jobs by passing all environment variables (e.g. ``PYTHONPATH``) to the job environments.

downward
^^^^^^^^
* Use write-once revision cache: instead of *cloning* the full FD repo
  into the revision cache only *copy* the ``src`` directory. This
  greatly reduces the time and space needed to cache revisions. As a
  consequence you cannot specify the destination for the clone
  anymore (the ``dest`` keyword argument is removed from the
  ``Translator``, ``Preprocessor`` and ``Planner`` classes) and only
  local FD repositories are supported (see
  :class:`downward.checkouts.HgCheckout`). After the files have been
  copied into the cache and FD has been compiled, a special file
  (``build_successful``) is written in the cache directory. When
  the cached revision is requested later an error is shown if this
  file is missing.
* Only use exit codes to reason about error reasons. Merge from FD master if your FD version does not produce meaningful exit codes.
* Preprocess parser: only parse logs and never output files.
* Never copy ``all.groups`` and ``test.groups`` files. Old Fast Downward branches need to merge from master.
* Always compress ``output.sas`` (also for ``compact=False``). Use ``xz`` for compressing.


v1.5
----

lab
^^^
* Add :func:`Experiment.add_fetcher()` method.
* If all columns have the same value in an uncolored table row, make all values bold, not grey.
* In :func:`Experiment.add_resource()` and :func:`Run.add_resource()` set ``dest=None`` if you don't want to copy or link the resource, but only need an alias to reference it in a command.
* Write and keep all logfiles only if they actually have content.
* Don't log time and memory consumption of process groups. It is still an unexplained error if too much wall-clock time is used.
* Randomize task order for grid experiments by default. Use ``randomize_task_order=False`` to disable this.
* Save wall-clock times in properties file.
* Do not replace underscores by dashes in table headers. Instead allow browsers to break lines after underscores.
* Left-justify string and list values in tables.

downward
^^^^^^^^
* Add optional *nick* parameter to Translator, Preprocessor and Planner classes. It defaults to the revision name *rev*.
* Save ``hg id`` output for each checkout and include it in reports.
* Add *timeout* parameter to :func:`DownwardExperiment.add_config()`.
* Count malformed-logs as unexplained errors.
* Pass ``legend_location=None`` if you don't need a legend in your plot.
* Pass custom benchmark directories in :func:`DownwardExperiment.add_suite()` by using the *benchmarks_dir* keyword argument.
* Do not copy logs from preprocess runs into search runs.
* Reference preprocessed files in run scripts instead of creating links if ``compact=True`` is given in the experiment constructor (default).
* Remove ``unexplained_error`` attribute. Errors are unexplained if ``run['error']`` starts with 'unexplained'.
* Remove ``*_error`` attributes. It is preferrable to inspect ``*_returncode`` attributes instead (e.g. ``search_returncode``).
* Make report generation faster (10-fold speedup for big reports).
* Add :func:`DownwardExperiment.add_search_parser()` method.
* Run ``make clean`` in revision-cache after compiling preprocessor and search code.
* Strip executables after compilation in revision-cache.
* Do not copy lab into experiment directories and grid-steps. Use the global lab version instead.


v1.4
----

lab
^^^
* Add :py:func:`exp.add_report() <lab.experiment.Experiment.add_report>` method to simplify adding reports.
* Use simplejson when available to make loading properties more than twice as fast.
* Raise default check-interval in Calls to 5s. This should reduce lab's overhead.
* Send mail when grid experiment finishes. Usage: ``MaiaEnvironment(email='mymail@example.com')``.
* Remove ``steps.Step.publish_reports()`` method.
* Allow creating nested new files in experiment directory (e.g. ``exp.add_new_file('path/to/file.txt')``).
* Remove duplicate attributes from reports.
* Make commandline parser available globally as :data:`lab.experiment.ARGPARSER` so users can add custom arguments.
* Add ``cache_dir`` parameter in :py:class:`Experiment <lab.experiment.Experiment>` for specifying where lab stores temporary data.

downward
^^^^^^^^
* Move ``downward.experiment.DownwardExperiment`` to ``downward.experiments.DownwardExperiment``, but keep both import locations indefinitely.
* Flag invalid plans in absolute reports.
* PlanningReport: When you append '_relative' to an attribute, you will get a table containing the attribute's values of each configuration relative to the leftmost column.
* Use bzip2 for compressing output.sas files instead of tar+gzip to save space and make opening the files easier.
* Use bzip2 instead of gzip for compressing experiment directories to save space.
* Color absolute reports by default.
* Use log-scale instead of symlog-scale for plots. This produces equidistant grid lines.
* By default place legend right of scatter plots.
* Remove ``--dereference`` option from tar command.
* Copy (instead of linking) PDDL files into preprocessed-tasks dir.
* Add table with Fast Downward commandline strings and revisions to AbsoluteReport.


v1.3
----

lab
^^^
* For Latex tables only keep the first two and last two hlines.

downward
^^^^^^^^
* Plots: Make category_styles a dictionary mapping from names to dictionaries of
  matplotlib plotting parameters to allow for more and simpler customization.
  This means e.g. that you can now change the line style in plots.
* Produce a combined domain- and problem-wise AbsoluteReport if ``resolution=combined``.
* Include info in AbsoluteReport if a table has no entries.
* Plots: Add ``params`` argument for specifying matplotlib parameters like
  font-family, label sizes, line width, etc.
* AbsoluteReport: If a non-numerical attribute is included in a domain-wise
  report, include some info in the table instead of aborting.
* Add :py:class:`Attribute <lab.reports.Attribute>` class for wrapping custom
  attributes that need non-default report options and aggregation functions.
* Parse ``expansions_until_last_jump`` attribute.
* Tex reports: Add number of tasks per domain with new ``\numtasks{x}`` command
  that can be cutomized in the exported texts.
* Add pgfplots backend for plots.


v1.2
----

lab
^^^
* Fetcher: Only copy the link not the content for symbolic links.
* Make properties files more compact by using an indent of 2 instead of 4.
* Nicer format for commandline help for experiments.
* Reports: Only print available attributes if none have been set.
* Fetcher: Pass custom parsers to fetcher to parse values from a finished experiment.
* For geometric mean calculation substitute 0.1 for values <= 0.
* Only show warning if not all attributes for the report are found in the evaluation dir,
  don't abort if at least one attribute is found.
* If an attribute is None for all runs, do not conclude it is not numeric.
* Abort if experiment path contains a colon.
* Abort with warning if all runs have been filtered for a report.
* Reports: Allow specifying a *single* attribute as a string instead of
  a list of one string (e.g. attributes='coverage').

downward
^^^^^^^^
* If compact=True for a DownwardExperiment, link to the benchmarks instead of copying them.
* Do not call ./build-all script, but build components only if needed.
* Fetch and compile sources only when needed: Only prepare translator and
  preprocessor for preprocessing experiments and only prepare planners for
  search experiments. Do it in a grid job if possible.
* Save space by deleting the benchmarks directories and omitting the search
  directory and validator for preprocess experiments.
* Only support using 'src' directory, not the old 'downward' dir.
* Use downward script regardless of other binaries found in the search directory.
* Do not try to set parent-revision property. It cannot be determined without
  fetching the code first.
* Make ProblemPlotReport class more general by allowing the get_points() method
  to return an arbitrary number of points and categories.
* Specify xscale and yscale (linear, log, symlog) in PlotReports.
* Fix removing downward.tmp.* files (use bash for globbing). This greatly reduces
  the needed space for an experiment.
* Label axes in ProblemPlots with ``xlabel`` and ``ylabel``.
* If a grid environment is selected, use all CPUs for compiling Fast Downward.
* Do not use the same plot style again if it has already been assigned by the user.
* Only write plot if valid points have been added.
* DownwardExperiment: Add member ``include_preprocess_results_in_search_runs``.
* Colored reports: If all configs have the same value in a row and some are None,
  highlight the values in green instead of making them grey.
* Never set 'error' to 'none' if 'search_error' is true.
* PlotReport: Add ``legend_location`` parameter.
* Plots: Sort coordinates by x-value for correct connections between points.
* Plots: Filter duplicate coordinates for nicer drawing.
* Use less padding for linear scatterplots.
* Scatterplots: Add ``show_missing`` parameter.
* Absolute reports: For absolute attributes (e.g. coverage)
  print a list of numbers of problems behind the domain name if not all configs
  have a value for the same number of problems.
* Make 'unsolvable' an absolute attribute, i.e. one where we consider problem
  runs for which not all configs have a value.
* If a non-numeric attribute is present in a domain-wise report, state its type
  in the error message.
* Let plots use the ``format`` parameter given in constructor.
* Allow generation of pgf plot files (only available in matplotlib 1.2).
* Allow generation of pdf and eps plots.
* DownwardReport: Allow passing a single function for ``derived_properties``.
* Plots: Remove code that sets parameters explicitly, sort items in legend.
* Add parameters to PlotReport that set the axes' limits.
* Add more items to downward FAQ.


v1.1
----

lab
^^^
* Add filter shortcuts: ``filter_config_nick=['lama', 'hcea'], filter_domain=['depot']`` (see :py:class:`Report <lab.reports.Report>`) (Florian)
* Ability to use more than one filter function (Florian)
* Pass an optional filter to :py:class:`Fetcher <lab.fetcher.Fetcher>` to fetch only a subset of results (Florian)
* Better handling of timeouts and memory-outs (Florian)
* Try to guess error reason when run was killed because of resource limits (Florian)
* Do not abort after failed commands by default
* Grid: When --all is passed only run all steps if none are supplied
* Environments: Support Uni Basel maia cluster (Malte)
* Add "pi" example
* Add example showing how to parse custom attributes
* Do not add resources and files again if they are already added to the experiment
* Abort if no runs have been added to the experiment
* Round all float values for the tables
* Add function :py:func:`lab.tools.sendmail` for sending e-mails
* Many bugfixes
* Added more tests
* Improved documentation

downward
^^^^^^^^
* Make the files output.sas, domain.pddl and problem.pddl optional for search experiments
* Use more compact table of contents for AbsoluteReports
* Use named anchors in AbsoluteReport (``report.html#expansions``, ``report.html#expansions-gripper``)
* Add colored absolute tables (see :py:class:`AbsoluteReport <downward.reports.absolute.AbsoluteReport>`)
* Do not add summary functions in problem-wise reports
* New report class :py:class:`ProblemPlotReport <downward.reports.plot.ProblemPlotReport>`
* Save more properties about experiments in the experiments's properties file for easy lookup (suite, configs, portfolios, etc.)
* Use separate table for each domain in problem-wise reports
* Sort table columns based on given config filters if given (Florian)
* Do not add VAL source files to experiment
* Parse number of reopened states
* Remove temporary downward files even if downward was killed
* Divide scatter-plot points into categories and lable them (see :py:class:`ScatterPlotReport <downward.reports.scatter.ScatterPlotReport>`) (Florian)
* Only add a highlighting and summary functions for numeric attributes in AbsoluteReports
* Compile validator if it isn't compiled already
* Downward suites: Allow writing SUITE_NAME_FIRST to run the first instance of all domains in SUITE_NAME
* LocalEnvironment: If ``processes`` is given, use as many jobs to compile the planner in parallel
* Check python version before creating preprocess experiment
* Add avg, min, max and stddev rows to relative reports
* Add RelativeReport
* Add :py:func:`DownwardExperiment.set_path_to_python() <downward.experiment.DownwardExperiment.set_path_to_python>`
* Many bugfixes
* Improved documentation

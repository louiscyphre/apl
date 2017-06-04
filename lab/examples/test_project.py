#! /usr/bin/env python

"""Testing script to choose between best configuration."""

import os
import os.path
import platform

from lab.environments import LocalEnvironment, MaiaEnvironment

from downward.experiment import FastDownwardExperiment
from downward.reports.absolute import AbsoluteReport
from downward.reports.scatter import ScatterPlotReport


ATTRIBUTES = ['coverage', 'expansions']

if 'cluster' in platform.node():
    # Create bigger suites with suites.py from the downward-benchmarks repo.
    SUITE = ['depot', 'freecell', 'gripper', 'zenotravel']
    ENV = MaiaEnvironment(priority=0)
else:
    SUITE = ['depot:p01.pddl', 'gripper:prob08.pddl']
    ENV = LocalEnvironment(processes=2)
# Change to path to your Fast Downward repository.
REPO = os.environ["DOWNWARD_REPO"]
REV  = 'default'
BENCHMARKS_DIR = os.environ["DOWNWARD_BENCHMARKS"]
REVISION_CACHE = os.path.expanduser('~/lab/revision-cache')

exp = FastDownwardExperiment(environment=ENV, revision_cache=REVISION_CACHE)
exp.add_suite(BENCHMARKS_DIR, SUITE)

exp.add_algorithm('iter-threshold-1', REPO, REV, 
    ['--heuristic', 'lmcount=lmcount()',
     '--heuristic', 'lmcount_a=lmcount(lm_hm(m=2),admissible=true)',
     '--heuristic', 'hmax=hmax()',
     '--heuristic', 'ff=ff()',
     '--search',
     'iterated([lazy(tiebreaking[lmcount, ff],preferred=[lmcount, ff]),\
               lazy_wastar([lmcount_a, hmax])],w=1,threshold=0.8,reopen_closed=false)'],
     driver_options=['--overall-time-limit', '30m' , '--overall-memory-limit', '2G'])

# Make a report (AbsoluteReport is the standard report).
exp.add_report(
    AbsoluteReport(attributes=ATTRIBUTES), outfile='report.html')

# Compare the number of expansions in a scatter plot.
#exp.add_report(
#    ScatterPlotReport(
#        attributes=["expansions"], filter_algorithm=["blind", "lmcut"]),
#S    outfile='scatterplot.png')

# Parse the commandline and show or run experiment steps.
exp.run_steps()

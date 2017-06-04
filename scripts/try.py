#! /usr/bin/env python

"""Solve some tasks with A* and the LM-Cut heuristic."""

import os
import os.path
import platform

from lab.environments import LocalEnvironment, MaiaEnvironment
#from lab.environments import MaiaEnvironment

from downward.experiment import FastDownwardExperiment
from downward.reports.absolute import AbsoluteReport
from downward.reports.scatter import ScatterPlotReport
from downward.reports.taskwise import TaskwiseReport
from downward.reports import PlanningReport

ATTRIBUTES = ['coverage', 'expansions']

if 'cluster' in platform.node():
    # Create bigger suites with suites.py from the downward-benchmarks repo.
    SUITE = ['depot', 'freecell', 'gripper', 'zenotravel']
    ENV = MaiaEnvironment(priority=0)
else:
    SUITE = ['depot:p02.pddl', 'gripper:prob02.pddl']
    ENV = LocalEnvironment(processes=2)
# Change to path to your Fast Downward repository.
REPO = os.environ["DOWNWARD_REPO"]
BENCHMARKS_DIR = os.environ["DOWNWARD_BENCHMARKS"]
#REVISION_CACHE = os.path.expanduser('~/lab/revision-cache')

exp = FastDownwardExperiment(environment=ENV, revision_cache=None)
exp.add_suite(BENCHMARKS_DIR, SUITE)

exp.add_algorithm('iterated', REPO, 'default', ['--heuristic', 'lmcount=lmcount(lm_hm(m=2))','--heuristic', 'lmcount_a=lmcount(lm_hm(m=2),admissible=true)','--heuristic', 'hmax=hmax()','--heuristic', 'ff=ff()','--search','iterated([lazy(tiebreaking([lmcount,ff]),preferred=[lmcount,ff]), lazy_wastar([lmcount_a, hmax],w=1,threshold=0.8,reopen_closed=false)])'], driver_options=['--overall-time-limit', '30m' , '--overall-memory-limit', '2G'])

exp.add_algorithm('iterated1', REPO, 'default', ['--heuristic', 'lmcount=lmcount(lm_hm(m=2))','--heuristic', 'lmcount_a=lmcount(lm_hm(m=2),admissible=true)','--heuristic', 'hmax=hmax()','--heuristic', 'ff=ff()','--search','iterated([lazy(tiebreaking([lmcount,ff]),preferred=[lmcount,ff]), lazy_wastar([lmcount_a, hmax],w=2,threshold=0.7,reopen_closed=false)])'], driver_options=['--overall-time-limit', '30m' , '--overall-memory-limit', '2G'])



#exp.add_report(PlanningReport(filter_algorithm=['lmcut', 'blind']))
exp.add_report(TaskwiseReport(
    attributes=["expansions", "total_time", "search_time","cost", "cost_all"],
    filter_algorithm=["iterated, iterated1"]))
# Parse the commandline and show or run experiment steps.
exp.run_steps()

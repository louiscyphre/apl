#! /usr/bin/env python

from __future__ import print_function

import multiprocessing
import os
import subprocess
import sys
import re
import fnmatch

import configs

DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(os.path.dirname(DIR),"fast-downward")
BENCHMARKS_DIR = os.path.join(REPO, "misc", "tests", "benchmarks2")
FAST_DOWNWARD = os.path.join(REPO, "fast-downward.py")

TASKS = []

for root, dirs, files in os.walk(BENCHMARKS_DIR):
    TASKS.extend([os.path.join(root, i) for i in files])  
    
    for file in TASKS:
       if fnmatch.fnmatch(file, '*domain*'):
           TASKS.remove(file)

# to try run all problems from easy to hard (currently wil not work because
# filenames are not consistent yet) 
tmp = sorted(TASKS, key=lambda item: (int(item.partition(' ')[0])
                                     if item[0].isdigit() else float('inf'), item))

TASKS[:] = []
TASKS = tmp

CONFIGS = {}
CONFIGS.update(configs.apl_satisficing_no_threshold())
CONFIGS.update(configs.apl_satisficing_with_threshold())

# if have issues with summary printing
#CONFIGS.update(configs.apl_satisficing_with_threshold_bad())

def run_and_print_summary(task, nick, config):
    cmd = [sys.executable, FAST_DOWNWARD]
    #cmd.extend(["--build",   "release64"])
    cmd.extend(["--overall-time-limit",   "30m"])
    cmd.extend(["--overall-memory-limit", "2G" ])
    cmd += [task] + config

    #print("\nRun {}:".format(cmd))

    # only config name printing
    print("\nconfigs.py: Running cofiguration {}:".format(nick))

    sys.stdout.flush()

    # if have issues with summary printing
    #subprocess.check_call(cmd)
    try:
        full_output =  subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except Exception, e:
        full_output = str(e.output)
    summary = re.findall(r"(Total time: [0-9]+.[0-9]+s|Plan cost: [\d]+|Search stopped without finding a solution.|Usage error occurred.|Time limit reached.|Memory limit has been reached.|caught signal [0-9]+ -- exiting|Completely explored state space -- no solution!|Tried to use unsupported feature.)",full_output)
    return summary


def cleanup():
    subprocess.check_call([sys.executable, FAST_DOWNWARD, "--cleanup"])


def main():
    # On Windows, ./build.py has to be called from the correct environment.
    # Since we want this script to work even when we are in a regular
    # shell, we do not build on Windows. If the planner is not yet built,
    # the driver script will complain about this.
    if os.name == "posix":
        jobs = multiprocessing.cpu_count()
        cmd = ["./build.py", "release32", "-j{}".format(jobs)]
        subprocess.check_call(cmd, cwd=REPO)
    for task in TASKS:
        print("\nRunning on ploblem {}:".format(task))
        for nick, config in CONFIGS.items():
                output = run_and_print_summary(task, nick, config)
                print(output)
                #output = validate_plans(task)
                #print(output)
                cleanup()

main()

#! /usr/bin/env python

from __future__ import print_function

import multiprocessing
import os
import subprocess
import sys
import re

import configs

DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(os.path.dirname(DIR),"fast-downward")
BENCHMARKS_DIR = os.path.join(REPO, "misc", "tests", "benchmarks")
FAST_DOWNWARD = os.path.join(REPO, "fast-downward.py")

TASKS = [os.path.join(BENCHMARKS_DIR, path) for path in [
    "gripper/prob01.pddl",
]]

CONFIGS = {}
CONFIGS.update(configs.configs_satisficing_extended())
CONFIGS.update(configs.apl_satisficing_with_threshold())

def run_and_print_summary(task, nick, config):
    cmd = [sys.executable, FAST_DOWNWARD]
    cmd.extend(["--overall-time-limit",   "30m"])
    cmd.extend(["--overall-memory-limit", "2G" ])
    cmd += [task] + config
    print("\nRun {}:".format(cmd))
    sys.stdout.flush()
    try:
        full_output =  subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except Exception, e:
        full_output = str(e.output)
    summary = re.findall(r"(Total time: [0-9]+.[0-9]+s|Plan cost: [\d]+|Search stopped without finding a solution.|Usage error occurred.|Time limit reached.)",full_output)
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
        #subprocess.check_call(cmd, cwd=REPO)
    for task in TASKS:
        for nick, config in CONFIGS.items():
                output = run_and_print_summary(task, nick, config)
                print(output)
                cleanup()

main()

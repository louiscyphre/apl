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
BENCHMARKS_DIR = os.path.join(REPO, "misc", "tests", "benchmarks")
FAST_DOWNWARD = os.path.join(REPO, "fast-downward.py")

TASKS = []

for root, dirs, files in os.walk(BENCHMARKS_DIR):
    TASKS += files

    for file in TASKS:
        if fnmatch.fnmatch(file, '*domain*'):
            TASKS.remove(file)

    for file in TASKS:
        if fnmatch.fnmatch(file, '*domain*'):
            TASKS.remove(file)

# to try run all problems from easy to hard 
tmp = sorted(TASKS, key=lambda item: (int(item.partition(' ')[0])
                                     if item[0].isdigit() else float('inf'), item))

#This neet to put in some for loop or something similar, we want full path to all .ppdl-s
#full_path_tmp = [os.path.join(root, path) for path in tmp]

TASKS[:] = []
TASKS = tmp
#TASKS = full_path_tmp

print(TASKS)

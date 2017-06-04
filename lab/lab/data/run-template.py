#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from lab.calls.call import Call
from lab.calls.log import driver_log, driver_err

sys.stdout = driver_log
sys.stderr = driver_err

from lab.calls.log import print_, redirects, save_returncode
from lab.calls.log import set_property

# Make sure we're in the run directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

set_property('queue', os.environ.get('QUEUE'))


"""CALLS"""

for stream in redirects.values():
    stream.close()

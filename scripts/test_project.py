#! /usr/bin/python

import os, fnmatch



def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


#find('domain.pddl', '/path')


def findi_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result




#!/usr/bin/python3
import re

with open("out.out","r") as old:
    lines = old.readlines()
    lines = [ line for line in lines if (line[0].isdigit() and line[len(line)-2].isdigit() and (line.count(" ")==1)) ]


with open("out.out","w") as new:
    for line in lines:
        new.write( line )



#!/usr/bin/python3
import re

with open("out.out","r") as old:
    lines = old.readlines()
    lines = [ line for line in lines if (line[0].isdigit() and line[len(line)-2].isdigit() and (line.count(" ")==1)) ]

#plancost = int( lines[0].split()[1] )
with open("out.out","w") as new:
    for line in lines:
        [s,g] = line.split(" ")
#        g = str( plancost - int(g) )
        new.write( s + " " + g )



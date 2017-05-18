#!/usr/bin/python3
with open("hash.out","r") as old:
    with open("stateDB.out","w") as new:
        for line in old.readlines():
            [h,g] = line.split(" ")
            g = str( 192 - int(g) )
            new.write(h + " " + g + "\n" )


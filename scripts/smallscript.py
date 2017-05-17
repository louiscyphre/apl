#!/usr/bin/python3
with open("hash1.out") as f1:
    hash1 = f1.readlines()
with open("hash2.out") as f2:
    hash2 = f2.readlines()
hash1 = [x.strip() for x in hash1]
hash2 = [x.strip() for x in hash2]
inter = set( hash1 ).intersection(hash2)
print("the intersection size is: " + str( len( inter )) )

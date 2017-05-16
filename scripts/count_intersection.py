#!/usr/bin/python3
with open("hash1.out","r") as f1:
    content1=f1.readlines()
with open("hash2.out","r") as f2:
    content2=f2.readlines()
content1=[x.strip() for x in content1]
content2=[x.strip() for x in content2]

inters = set( content1 ).intersection( content2 )
print( str( len(list(inters)) ))

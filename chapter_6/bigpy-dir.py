"""
Find the largest Python source file in a single directory.
Search Windows Python source lib, unless dir command-line arg.
"""
import os, glob, sys

allsizes = []
allpy = glob.glob("../")
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))
    allsizes.sort()

print(allsizes[:2])
print(allsizes[-2:])

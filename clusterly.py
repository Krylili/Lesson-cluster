#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:19:43 2019

@author: Presenter
"""

import happy
import csv

filename = "results100.csv"


# Open the file
datafile = open(filename, "r")

# prepare a list
offsets = [0]

# read line by line from file
# for each line do the following:
line = datafile.readline()
while line != "":
# - ask the current reading position
    pos = datafile.tell()
# - add the position to a list
    offsets.append(pos)
    # read a new line from the file
    line = datafile.readline()
    
del offsets[-1]

# print the list
print(offsets)

# Have a test set of line numbers
testlist = [5, 31, 8, 10, 22, 52, 100, 42, 90, 56, 6]

# pull out the lines of this test set
for lineno in testlist:
    datafile.seek(offsets[lineno-1])
    line = datafile.readline()
    print(line[0:30])
    
    


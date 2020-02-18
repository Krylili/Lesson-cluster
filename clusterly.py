#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:19:43 2019

@author: Presenter
"""

import happy
import scipy.cluster.hierarchy as scihi

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

# Get dataset for a certain offset in a file
def getdataset(datafile: "File reference", offset: int) -> dict:
    # Jump to offset in datafile
    datafile.seek(offset)
    
    # Read line into a string
    line = datafile.readline()
    
    # Split elments of line into a list
    elements = line.split("\t")
    
    # Keys of the dictionary
    keys = ["datasetid", "seq_id", "seq_len", "sequence",
            "quality_score", "quality_seq"]
    
    dataset = dict(zip(keys, elements))
    dataset.update({"offset": offset})
    
    return dataset
    
    

# pull out the lines of this test set
for lineno in testlist:
    dataset = getdataset(datafile, offsets[lineno-1])
    print(dataset)
    
    


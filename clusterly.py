#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:19:43 2019

@author: Presenter
"""

import happy
import scipy.cluster.hierarchy as scihi
import matplotlib.pyplot as plt

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
    

# Function to calculate the distance between two elements
def distfunction(offset1: int, offset2: int) -> int:
    dataset1 = getdataset(datafile, offset1)
    dataset2 = getdataset(datafile, offset2)
    
    return happy.levenshtein_distance(dataset1["sequence"],
                                      dataset2["sequence"],
                                      Damerau=True)
    
    
# Function to return the sequence for a certain offset
def labelfunction(clusterindex: int) -> str:
    dataset = getdataset(datafile, offsets[clusterindex])    
    return dataset["sequence"]
    

# Set up starting cluster
startclusters = [[offsets[n]] for n in range(20)]

# Calculate matrix and show dendrogram
Z = scihi.linkage(startclusters, method="single", metric=distfunction)
scihi.dendrogram(Z, orientation="left", leaf_label_func=labelfunction)
plt.show()

    
    
    

    

    


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Happy is a nice module that allows us to calculate the Levenshtein distance.


License 
-------
licensed under GPLv3

Authors
-------
People of 'Adventures on Python' course

Installation
-------------
Just copy the file in the same directory as your main program and import it!

"""

from typing import List


COST_PER_OPERATION = 1
"""Cost of a single edit operation."""


def levenshtein_distance(source: str, target: str, Damerau: bool = True) -> int:
    """
    Calculates the Levenshtein distance using an iterative approach.
    
    Arguments:
        source:  string A from which to edit from
        target:  string B to which to edit to
        
    Return:
        Returns an integer with the respective Levenshtein distance.
        
    Cost of a single operation is defined by `happy.COST_PER_OPERATION`.    
    """
    # Corner case 1: source and target are equal, i.e
    # Levenshtein distance is zero
    if source == target:
        return 0
    
    # Corner case 2: one of the strings is empty, i.e.
    # the Levenshtein distance is the length of the non-
    # empty string
    if len(source) == 0:
        return len(target)
    
    if len(target) == 0:
        return len(source)
    
    # Two dimensional list (=matrix) to hold the distances
    # calculated for the substrings
    distances = [[0 for x in range(len(target)+1)] for y in range(len(source)+1)]
    
    # Fill first row with lengths of respective substrings
    for x in range(len(target)+1):
        distances[0][x] = x
        
    # Calculate row by row
    for y in range(len(source)+1):
        if y == 0:
            continue
        
        # First element = length of substring
        distances[y][0] = y
        
        for x in range(len(target)+1):
            if x == 0:
                continue
            
            # reference points to the left, topleft, and top
            references = [distances[y][x-1], 
                          distances[y-1][x-1], 
                          distances[y-1][x]]
            
            # Check if current letter in source and target are equal
            if source[y-1] == target[x-1]:
                distances[y][x] = references[1]
            else:
                distances[y][x] = min(references) + COST_PER_OPERATION      
    
    
    # Return final distance, which is in the bottom right element
    return distances[-1][-1]


FASTQ_NOERROR = 0
FASTQ_ERROR_NO4LINES = 1
FASTQ_ERROR_SEQLENMISMATCH = 2
FASTQ_ERROR_NOATSIGN = 3
FASTQ_ERROR_NOPLUSSIGN = 4

# Read four lines of a FASTQ file and convert it into a dictionary
def convert_FASTQ_into_dictionary(lines: List[str]) -> (dict, int):
    if not len(lines) == 4:
        return {}, FASTQ_ERROR_NO4LINES
    
    if not len(lines[1]) == len(lines[3]):
        return {}, FASTQ_ERROR_SEQLENMISMATCH
    
    if not lines[0].startswith("@"):
        return {}, FASTQ_ERROR_NOATSIGN
    
    if not lines[2].startswith("+"):
        return {}, FASTQ_ERROR_NOPLUSSIGN
    
    # TODO: second line has to be an actual NA sequence
    #       fourth line has to be a quality score sequence
    
    dataset = { "Sequence ID": lines[0][1:],
                "Sequence": lines[1],
                "Quality sequence": lines[3] }
    
    return dataset, FASTQ_NOERROR
    
# Calculate the fraction of bases that are above a certain quality threshold
def Phredy_quality_fraction(qualitysequence: str, threshold: int = 30) -> float:
    # Check if qualitysequence is empty
    if len(qualitysequence) == 0:
        return 0.0
    
    # set up counter with zero
    counter = 0
    # For each letter in the sequence do the following
    for letter in qualitysequence:
    # - translate letter into a score
        score = ord(letter) - ord("!")
    # - if score is larger than threshold do the following
        if score > threshold:            
    # - - increase counter
            counter += 1
            
    # return counter over length of sequence
    return counter/len(qualitysequence)


# Recursion approach
#def levenshtein_distance_rec(source: str, target: str) -> int:
#    # Corner case 1: source and target are equal, i.e
#    # Levenshtein distance is zero
#    if source == target:
#        return 0
#    
#    # Corner case 2: one of the strings is empty, i.e.
#    # the Levenshtein distance is the length of the non-
#    # empty string
#    if len(source) == 0:
#        return len(target)
#    
#    if len(target) == 0:
#        return len(source)
#    
#    # Calculate cost for substitution
#    cost = 0
#    if source[-1] != target[-1]:
#        cost = 1
#    
#    # Calculate the LDs for three operations
#    delete = levenshtein_distance(source[:-1], target) + 1
#    insert = levenshtein_distance(source, target[:-1]) + 1
#    substi = levenshtein_distance(source[:-1], target[:-1]) + cost 
#    
#    # Return the minimum of all three operations
#    return min([delete, insert, substi])



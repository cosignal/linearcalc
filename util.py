"""
Module Name: util.py
Description: This module contains various helper functions, such
             as those for displaying matrices or changing data
             types.
Author: James Hansen
Created: 8/23/24
"""

from copy import deepcopy

def index_of_match(list, match):
    return next((i for i, elt in enumerate(list) if elt == match), -1)

def floatify_matrix(matrix):
    m = deepcopy(matrix)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            m[row][col] = float(m[row][col])
    return m

"""
Module Name: space.py
Description: This module contains functionality for determining the
             column/row space (and rank), null space (and nullity),
             and linear independence of the column/row vectors of a matrix.
Author: James Hansen
Created: 8/23/24
"""

from util import index_of_match
from rref import rref, pivots

def initialize_null_space(cols, frees):
    # initializes null space list based on columns corresponding to free variables
    frees_copy = frees.copy()
    null_space = [[0 for _ in range(cols)] for _ in range(len(frees_copy))]

    for row_idx in range(len(null_space)):
        for col_idx in range(len(null_space[row_idx])):
            if (col_idx == frees_copy[0]):
                null_space[row_idx][frees_copy[0]] = 1
                frees_copy.pop(0)
                break

    return null_space

def null_space_reduced(matrix):
    # null space for matrix in RREF
    cols = len(matrix[0]) # assumes well-formed matrix
    pivs = pivots(matrix)
    pivot_cols = [elt[1] for elt in pivs]
    frees = [elt for elt in range(cols) if elt not in pivot_cols]
    null_space = initialize_null_space(cols, frees)

    for pivot in pivs:
        for col_idx in range(cols):
            reached_pivot = False
            row = matrix[pivot[0]]
            if (not reached_pivot):
                if ((row[col_idx] == 1) and (col_idx == pivot[1])):
                    reached_pivot = True
                    continue
                val = row[col_idx]
                if (val != 0):
                        free_idx = index_of_match(frees, col_idx)
                        null_space[free_idx][pivot[1]] = -val
    return null_space

def null_space(matrix):
    # returns list of vectors representing the null space of the matrix
    m = matrix.copy()
    return null_space_reduced(rref(m))

def nullity_reduced(matrix):
    # returns dimension (number of vectors) of the null space for RREF matrix
    return len(null_space_reduced(matrix))

def nullity(matrix):
    # returns dimension (number of vectors) of the null space for non-reduced matrix
    return len(null_space(matrix))

def linear_independence(vectors):
    # returns true if the given set of vectors are linearly independent
    return

def row_space(matrix):
    # TODO
    return

def col_space(matrix):
    # TODO
    return

def rank(matrix):
    # TODO
    return

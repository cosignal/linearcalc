"""
Module Name: factorizations.py
Description: This module contains functionality for finding various
             factorizations of a matrix, including but not limited
             to: LU, QR, and SVD.
Author: James Hansen
Created: 8/23/24
"""

from fractions import Fraction
from inverse import identity
from rref import add_row_multiple

# TODO: QR, SVD (what else?)

def lu_square(matrix):
    # FIXME: not all squares have an LU, this needs to be accounted for here
    if (len(matrix) != len(matrix[0])): # assumes well-formed input
        print("LU decomposition can only be performed on a square matrix")
        return
    
    l = identity(len(matrix))
    u = matrix.copy()

    for col_idx in range(len(u[0])):
        for row_idx in range(col_idx+1, len(u)):
            scalar = Fraction(u[row_idx][col_idx], u[col_idx][col_idx])
            l[row_idx][col_idx] = scalar
            u[row_idx] = add_row_multiple(u[col_idx],u[row_idx],-scalar)

    return [l,u]

def lu(matrix):
    # returns an array containing two matrices, the first is L and the second is U
    if (len(matrix) == len(matrix[0])): # assumes well-formed input
        lu_square(matrix)
    else: # TODO: non-squares... a possibly involved topic of study
        print("sorry, I'm too much of a square for this")
        return

"""
Module Name: eigenvectors.py
Description: This module contains functionality for examining the 
             eigenspace associated with a matrix.
Author: James Hansen
Created: 8/23/24
"""

from sympy import Symbol, expand
from numpy import roots, round
from numpy.polynomial import Polynomial
from matrix_arithmetic import scale_matrix, subtract_matrices
from inverse import identity
from determinant import determinant
from space import null_space

def characteristic(matrix):
    # returns a characteristic matrix corresponding to the given matrix
    m = matrix.copy()
    
    if (len(m) != len(m[0])): # assumes well-formed input
        print("cannot find eigenvalues of non-square matrix")
        return
    
    lambda_identity = scale_matrix(Symbol('lambda'), identity(len(m)))
    return subtract_matrices(m, lambda_identity)

def singular(characteristic, eigenvalue):
    # substitutes lambda with eigenvalue for characteristic matrix 
    singular = characteristic.copy()
    for row_idx in range(len(singular)):
        for col_idx in range(len(singular[0])):
            if (row_idx == col_idx):
                entry = singular[row_idx][col_idx].subs('lambda',eigenvalue)
                singular[row_idx][col_idx] = entry
    return singular

def eigenvalues(matrix, is_characteristic=False):
    # returns array of eigenvalues for the given matrix

    if (is_characteristic):
        characteristic_matrix = matrix
    else:
        characteristic_matrix = characteristic(matrix)

    expanded = Poly(expand(determinant(characteristic_matrix)))
    coeffs = expanded.coeffs()

    if (coeffs[0] < 0):
        neg_expanded = -expanded
        coeffs = neg_expanded.coeffs()

    # NOTE: rounding here due to floating point precision in np.coeffs()
    # (this may just be a quick fix and worth revising)
    eigenvalues = round(roots(coeffs), decimals=8)

    return eigenvalues
    
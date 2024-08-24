"""
Module Name: inverse.py
Description: This module contains functionality for finding the 
             inverse of a matrix and for working with identity 
             matrices.
Author: James Hansen
Created: 8/23/24
"""

from matrix_arithmetic import is_equal_matrix
from determinant import determinant
from rref import rref

def augment_square(matrix_A, matrix_B):
    # augments matrix A with matrix B
    if (len(matrix_A) != len(matrix_A[0])) or (len(matrix_B) != len(matrix_B[0])):
        print("Both matrices must be square!")
        return
    if (len(matrix_A) != len(matrix_B)) and (len(matrix_A[0]) != len(matrix_B[0])):
        print("Matrices should be of equal dimension!")
        return
    
    augmented = []
    for row in range(len(matrix_A)):
        augmented_row = matrix_A[row].copy()
        for col in range(len(matrix_A[0])):
            augmented_row.append(matrix_B[row][col])
        augmented.append(augmented_row)
    
    return augmented

def identity(dimension):
    # return identity matrix of specified dimension
    if dimension == 1:
        return [[1]]
    identity = []
    for row in range(dimension):
        identity_row = []
        for col in range(dimension):
            if row == col:
                identity_row.append(1)
            else:
                identity_row.append(0)
        identity.append(identity_row)
    return identity

def is_identity(matrix):
    # NOTE: assumes well-formed matrix
    if len(matrix) != len(matrix[0]):
        print("Identity matrices must be square")
        return False
    return is_equal_matrix(matrix, identity(len(matrix)))

def disaugment_square(augmented):
    size = int(len(augmented[0]) / 2)
    sub = []
    for i in range(len(augmented)):
        sub_row = []
        for j in range(size):
            sub_row.append(augmented[i][j + size])
        sub.append(sub_row)
    return sub

def invert_matrix(matrix):
    if determinant(matrix) == 0:
        print("Determinant is zero, matrix is singular")
        return
    if len(matrix) != len(matrix[0]):
        print("Matrix must be square to be invertible")
        return

    augmented = augment_square(matrix, identity(len(matrix)))
    reduced = rref(augmented)
    return disaugment_square(reduced)

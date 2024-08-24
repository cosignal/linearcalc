"""
Module Name: determinant.py
Description: This module contains functionality for finding the 
             determinant of a matrix.
Author: James Hansen
Created: 8/23/24
"""

def square_sub_matrix(matrix, excluded_col):
    # NOTE: this might not be as general as the name suggests
    #       (given the excluded row 0 assumption)
    sub = []
    for row in range(1, len(matrix)):
        sub_row = []
        for col in range(len(matrix[0])):
            if col == excluded_col:
                continue
            sub_row.append(matrix[row][col])
        sub.append(sub_row)
    return sub

def two_by_two_det(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det = a*d - b*c
    return det

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print("Only square matrices have determinants!")
        return
    
    if len(matrix) == 2:
        return two_by_two_det(matrix)
    
    det = 0
    for col_index in range(len(matrix[0])):
        entry = matrix[0][col_index]
        if col_index%2 == 0:
            coeff = entry
        else:
            coeff = -entry
        sub = square_sub_matrix(matrix, col_index)
        det += coeff*determinant(sub)

    return det

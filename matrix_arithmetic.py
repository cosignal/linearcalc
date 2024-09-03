"""
Module Name: matrix_arithmetic.py
Description: This module contains functions to perform elementary 
             arithmetic-like operations on matrices such as addition,
             subtraction, various forms of scaling, and transpose.
Author: James Hansen
Created: 8/23/24
"""

def add_rows(row_A, row_B):
    if len(row_A) != len(row_B):
        print("rows must have equal length to add")
        return
    sum = []
    for entry in range(len(row_A)):
        sum.append(row_A[entry]+row_B[entry])
    return sum

def add_matrices(matrix_A, matrix_B):
    rows = len(matrix_A)
    columns = len(matrix_A[0])
    sum = []

    if rows != len(matrix_B):
        print("matrices must have equal number of rows")
        return
    if columns != len(matrix_B[0]):
        print("matrices must have equal number of columns")
        return
    
    for row in range(rows):
        new_row = []
        for column in range(columns):
            new_row.append(matrix_A[row][column]+matrix_B[row][column])
        sum.append(new_row)

    return sum

def subtract_matrices(matrix_A, matrix_B):
    # matrix_A - matrix_B
    rows = len(matrix_A)
    columns = len(matrix_A[0])
    difference = []

    if rows != len(matrix_B):
        print("matrices must have equal number of rows")
        return
    if columns != len(matrix_B[0]):
        print("matrices must have equal number of columns")
        return
    
    for row in range(rows):
        new_row = []
        for column in range(columns):
            new_row.append(matrix_A[row][column]-matrix_B[row][column])
        difference.append(new_row)
    
    return difference

def multiply_matrices(matrix_A, matrix_B):
    product = []
    if len(matrix_A[0]) != len(matrix_B):
        print("dimension mismatch")
        return
    
    for A_row in range(len(matrix_A)):
        product_row = []
        for B_col in range(len(matrix_B[0])):
            sum = 0
            for B_row_index in range(len(matrix_B)):
                A_entry_index = B_row_index
                sum += matrix_A[A_row][A_entry_index]*matrix_B[B_row_index][B_col]
            product_row.append(sum)
        product.append(product_row)
    return product

def is_equal_matrix(matrix_A, matrix_B):
    if (len(matrix_A) != len(matrix_B)) or (len(matrix_A[0]) != len(matrix_B[0])):
        print("dimension mismatch")
        return False
    equal = False
    for row in range(len(matrix_A)):
        for col in range(len(matrix_A[0])):
            equal = matrix_A[row][col] == matrix_B[row][col]
    return equal

def scale_row (scalar, row_vec):
    scaled_row = []
    for entry in range(len(row_vec)):
        scaled_row.append(scalar*row_vec[entry])
    return scaled_row

def scale_matrix(scalar, matrix):
    scaled_matrix = []
    for row in range(len(matrix)):
        scaled_row = scale_row(scalar, matrix[row])
        scaled_matrix.append(scaled_row)
    return scaled_matrix

def transpose(matrix):
    tpose = []
    for column in range(len(matrix[0])):
        t_row = []
        for row in range(len(matrix)):
            t_row.append(matrix[row][column])
        tpose.append(t_row)
    return tpose

def trace(matrix):
    trace = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if (row == col):
                trace += matrix[row][col]
    return trace

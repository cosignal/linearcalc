"""
Module Name: rref.py
Description: This module contains functionality for reduction of
             matrices to echelon form.
Author: James Hansen
Created: 8/23/24
"""

from fractions import Fraction
from matrix_arithmetic import scale_row, add_rows
from vectors import is_zero_vector

def pivot_cols(matrix):
    # given a reduced matrix, return an array of indices of pivot columns
    pivots = []
    for row_idx in range(len(matrix)):
        if (is_zero_vector(matrix[row_idx])):
            break
        for col_idx in range(len(matrix[row_idx])):
            if (matrix[row_idx][col_idx] == 1):
                pivots.append(col_idx)
                break
    return pivots

def divide_row(row, divisor):
    return scale_row(Fraction(1, divisor), row)

def swap_rows(matrix, row_A_index, row_B_index):
    if row_A_index == row_B_index:
        print("cannot swap row with itself")
        return
    m = matrix.copy()
    row_A = m[row_A_index]
    row_B = matrix[row_B_index]
    matrix[row_A_index] = row_B
    matrix[row_B_index] = row_A
    return matrix

def add_row_multiple(row_A, row_B, scalar):
    return add_rows(scale_row(scalar, row_A), row_B)

def pivot_row_idx(matrix, row_idx, col_idx):
    col = [row[col_idx] for row in matrix]
    col_max = max(col, key=abs)
    for row_idx in range(row_idx, len(matrix)):
        if ((matrix[row_idx][col_idx] == col_max) or
            (matrix[row_idx][col_idx] == 1)):
            return row_idx

def rref(matrix):
     # NOTE: assumes well-formed matrix
    m = matrix.copy()
    row_idx = 0
    for col_idx in range(len(m[0])):
        if (is_zero_vector(m[row_idx])):
            swap_rows(m, row_idx, row_idx+1)

        pivot_row = pivot_row_idx(m, row_idx, col_idx)
        if (pivot_row != row_idx):
            swap_rows(m, pivot_row, row_idx)

        if (m[row_idx][col_idx] != 1):
            m[row_idx] = divide_row(m[row_idx], m[row_idx][col_idx])

        for row in range(len(m)):
            if ((row != row_idx) and (m[row][col_idx] != 0)):
                m[row] = add_row_multiple(m[row_idx], m[row], -m[row][col_idx])

        row_idx += 1
        if (((row_idx == len(m)-1) and
             is_zero_vector(m[row_idx])) or
            (row_idx >= len(m))):
            break

    return m

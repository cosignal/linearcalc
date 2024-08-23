import numpy as np
import math as math
from fractions import Fraction

# TODO: currently everything for this project is in this file
# eventually I want to split things up into separate files
# this file will contain code for an interface that will 
# call the calculator functions and such from the other files
# at first that can just be a command line interface 
# eventually there can be a UI

# make matrix
# TODO: figure out how to ensure properly formatted input
""" def make_matrix_type1():
# make matrix based on colon-separated rows
# specifying number of rows/cols from user not necessary
    while True:
        print("separate entries by commas, and rows by semicolons")
        rows = input().split(";")
        row_count = len(rows) """

def make_matrix_type2():
    print("enter number of rows")
    rows = int(input())
    print("enter number of columns")
    columns = int(input())
    number_of_entries = rows*columns
    matrix = np.empty((0,columns))

    while True:
        print("enter each entry, separated by spaces, in column/row order from left to right and top to bottom")
        entries_input = input().split()
        if len(entries_input) == number_of_entries:
            break
        else:
            print("for a(n) " + str(rows) + "x" + str(columns) + " matrix, please provide " + str(number_of_entries) + " entries")
    # what about other invalid inputs? (e.g. non-integers, other symbols)

    entry_count = 0
    for i in range(rows):
        new_row = []
        for j in range(columns):
            new_row.append(int(entries_input[entry_count]))
            entry_count += 1
        matrix = np.vstack([matrix, new_row])

    print(matrix)
    return matrix

# matrix arithmetic

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
    sum = np.empty((0,columns))

    if rows != len(matrix_B):
        print("matrices must have equal number of rows")
        return
    if columns != len(matrix_B[0]):
        print("matrices must have equal number of columns")
        return
    
    for row in range(rows):
        new_row = []
        for column in range(columns):
            new_row.append(matrix_A[row,column]+matrix_B[row,column])
        sum = np.vstack([sum, new_row])
    
    return sum

def subtract_matrices(matrix_A, matrix_B):

    rows = len(matrix_A)
    columns = len(matrix_A[0])
    difference = np.empty((0,columns))

    if rows != len(matrix_B):
        print("matrices must have equal number of rows")
        return
    if columns != len(matrix_B[0]):
        print("matrices must have equal number of columns")
        return
    
    for row in range(rows):
        new_row = []
        for column in range(columns):
            new_row.append(matrix_A[row,column]-matrix_B[row,column])
        difference = np.vstack([difference, new_row])
    
    return difference

def multiply_matrices(matrix_A, matrix_B):
    product = np.empty((0, len(matrix_B[0])))
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
        product = np.vstack([product, product_row])
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

# matrix manipulation

def transpose(matrix):
    tpose = np.empty((0, len(matrix)))
    for column in range(len(matrix[0])):
        t_row = []
        for row in range(len(matrix)):
            t_row.append(matrix[row][column])
        tpose = np.vstack([tpose, t_row])
    return tpose

def scale_row (scalar, row_vec):
    scaled_row = []
    for entry in range(len(row_vec)):
        scaled_row.append(scalar*row_vec[entry])
    return scaled_row

def scale_matrix(scalar, matrix):
    scaled_matrix = np.empty((0,len(matrix[0])))
    for row in range(len(matrix)):
        scaled_row = scale_row(scalar, matrix[row])
        scaled_matrix = np.vstack([scaled_matrix, scaled_row])
    return scaled_matrix

# matrix reduction / RREF

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

def floatify_matrix(matrix):
    m = matrix.copy()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            m[row][col] = float(m[row][col])
    return m

def pivot_row_idx(matrix, col_idx):
    col = [row[col_idx] for row in matrix]
    col_max = max(col, key=abs)
    for row_idx in range(len(matrix)):
        if ((matrix[row_idx][col_idx] == col_max) or
            (matrix[row_idx][col_idx] == 1)):
            return row_idx

def is_zero_row(row):
    return all((entry == 0) for entry in row)

def rref(matrix):
     # NOTE: assumes well-formed matrix
    m = matrix.copy()
    row_idx = 0
    for col_idx in range(len(m[0])):

        if (is_zero_row(m[row_idx])):
            swap_rows(m, row_idx, row_idx+1)

        pivot_row = pivot_row_idx(m, col_idx)

        if (pivot_row != row_idx):
            swap_rows(m, pivot_row, row_idx)

        if (m[row_idx][col_idx] != 1):
            m[row_idx] = divide_row(m[row_idx], m[row_idx][col_idx])

        for row in range(len(m)):
            if ((row != row_idx) and (m[row][col_idx] != 0)):
                m[row] = add_row_multiple(m[row_idx], m[row], -m[row][col_idx])

        row_idx += 1
        if (((row_idx == len(m)-1) and
             is_zero_row(m[row_idx])) or
            (row_idx >= len(m))):
            break

    return m

# determinant

def square_sub_matrix(matrix, excluded_col):
    # NOTE: this might not be as general as the name suggests, given the excluded row 0 assumption
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

# inverse

def augment_square(matrix_A, matrix_B):
    if (len(matrix_A) != len(matrix_A[0])) or (len(matrix_B) != len(matrix_B[0])):
        print("Both matrices must be square!")
        return
    if (len(matrix_A) != len(matrix_B)) and (len(matrix_A[0]) != len(matrix_B[0])):
        print("Matrices should be of equal dimension!") # NOTE: unnecessary?
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
    # NOTE: this assumes that every row has the same length, which will 
    # be true for a well-formed matrix, but may not be true for every 2D 
    # array that can be passed to this function
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

# vectors
# NOTE: here the dot product is being used. consider generalizing
# this functionality to any provided Euclidian Inner Product

def scale_vector(scalar, vec):
    scaled_vec = []
    for i in range(len(vec)):
        scaled_vec.append(scalar*vec[i])
    return scaled_vec

def add_vectors(vec_A, vec_B):
    if len(vec_A) != len(vec_B):
        print("vectors must be of equal dimension to add")
        return
    sum = []
    for i in range(len(vec_A)):
        sum.append(vec_A[i]+vec_B[i])
    return sum

def subtract_vectors(vec_A, vec_B):
    # vec_A-vec_B
    if len(vec_A) != len(vec_B):
        print("vectors must be of equal dimension to subtract")
        return
    diff = []
    for i in range(len(vec_A)):
        diff.append(vec_A[i]-vec_B[i])
    return diff

def dot_product(vec_A, vec_B):
    if len(vec_A) != len(vec_B):
        print("vectors must be of equal dimension to dot")
        return
    prod = 0
    for i in range(len(vec_A)):
        prod += vec_A[i]*vec_B[i]
    return prod

def is_orthogonal_vec(vec_A, vec_B):
    return dot_product(vec_A, vec_B) == 0

def magnitude(vec):
    return math.sqrt(dot_product(vec, vec))

def angle_rads(vec_A, vec_B):
    return math.acos(dot_product(vec_A, vec_B)/(magnitude(vec_A)*magnitude(vec_B)))

def angle_degrees(vec_A, vec_B):
    return (180*angle_rads(vec_A, vec_B))/math.pi

def distance(vec_A, vec_B):
    diff = subtract_vectors(vec_A, vec_B)
    return math.sqrt(dot_product(diff, diff))

def scalar_projection(vec_A, vec_B):
    # A onto B
    return dot_product(vec_A, vec_B)/magnitude(vec_B)

def vector_projection(vec_A, vec_B):
    # the orthogonal projection of A onto B
    scalar = dot_product(vec_A, vec_B)/dot_product(vec_B, vec_B)
    return scale_vector(scalar, vec_B)

def normalize(vec):
    return scale_vector((1/magnitude(vec)), vec)

# orthogonal matrices (orthonormal basis)

def is_orthogonal_matrix(matrix):
    return is_identity(multiply_matrices(transpose(matrix), matrix))

# TODO: the vectors argument passed to gram_schmidt is an array of the vectors 
# to be orthonormalized, where each vector is an array, so when using this
# function on a matrix, the column vectors of that matrix should be passed,
# and this can be done simply by passing the transpose of the matrix 
# it might make sense to ensure vectors has more than one entry,
# also that the vecs are of equal dimension, oh and also that the 
# vectors are not already orthonormal!
# NOTE: it feels like I kinda cheesed it but I avoided float precision issue
# by using fraction representation
def gram_schmidt(vectors):
    u = []
    e = []
    for vec in range(len(vectors)):
        if vec == 0:
            u.append(vectors[vec])
            e.append(normalize(vectors[vec]))
            continue
        u.append(vectors[vec])
        for diff in range(vec):
            proj = vector_projection(vectors[vec], u[diff])
            u[vec] = subtract_vectors(u[vec], proj)
        e.append(normalize(u[vec]))
    return e

# NOTE: to normalize is to make a vector with a norm of 1
# you can't do that to the zero vector 
# so account for that and discard zero vectors

def vector_projection_frac(vec_A, vec_B):
    # the orthogonal projection of A onto B
    scalar = Fraction(dot_product(vec_A, vec_B), dot_product(vec_B, vec_B))
    return scale_vector(scalar, vec_B)

def gram_schmidt_frac(vectors):
    u = []
    e = []
    for vec in range(len(vectors)):
        if vec == 0:
            u.append(vectors[vec])
            e.append(normalize(vectors[vec]))
            continue
        u.append(vectors[vec])
        for diff in range(vec):
            proj = vector_projection_frac(vectors[vec], u[diff])
            u[vec] = subtract_vectors(u[vec], proj)
        e.append(normalize(u[vec]))
    return e

#

# eigenvectors (CAS needed)

# factorizations (LU, QR, SVD)

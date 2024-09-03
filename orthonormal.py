"""
Module Name: orthonormal.py
Description: This module contains functionality for creating 
             orthonormal sets of vectors using the Gram-Schmidt
             process.
Author: James Hansen
Created: 8/23/24
"""

from fractions import Fraction
from inverse import is_identity
from matrix_arithmetic import multiply_matrices, transpose
from vectors import dot_product, scale_vector, normalize, subtract_vectors

def is_orthogonal_matrix(matrix):
    return is_identity(multiply_matrices(transpose(matrix), matrix))

# NOTE: the vectors argument passed to gram_schmidt is an array of the vectors 
# to be orthonormalized, where each vector is an array, so when using this
# function on a matrix, the column vectors of that matrix should be passed,
# and this can be done simply by passing the transpose of the matrix 

# TODO: ensure that 'vectors' has more than one entry,
#  that they are of equal dimension, 
#  that they are not already orthonormal,
#  and discard zero vectors to avoid illegal division

def vector_projection_frac(vec_A, vec_B):
    # the orthogonal projection of A onto B
    scalar = Fraction(dot_product(vec_A, vec_B), dot_product(vec_B, vec_B))
    return scale_vector(scalar, vec_B)

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
            proj = vector_projection_frac(vectors[vec], u[diff])
            u[vec] = subtract_vectors(u[vec], proj)
        e.append(normalize(u[vec]))
    return e

def orthogonal_complement(vectors):
    # TODO
    return

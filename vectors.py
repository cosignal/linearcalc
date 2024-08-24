"""
Module Name: vectors.py
Description: This module contains functionality for performing 
             vector arithmetic and projections.
Author: James Hansen
Created: 8/23/24
"""

# NOTE: here the standard dot product is being used, consider how 
#       this would be generalized to accomodate any given (valid)
#       definition for a Euclidian Inner Product

import math

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
    # NOTE: the zero vector cannot be normalized
    return scale_vector((1/magnitude(vec)), vec)

import math as math
from fractions import Fraction

# TODO: separate into modules

# TODO: use this file for CLI code

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

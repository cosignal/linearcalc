"""
Module Name: basis.py
Description: This module contains functionality related to basis
             vectors, coordinate systems, and change-of-basis.
Author: James Hansen
Created: 8/23/24
"""

from inverse import augment_square, disaugment_square, identity
from rref import rref

# TODO: research what else could be relevant here

def basis(vectors):
    # returns the basis of the space spanned by the set of given vectors
    # TODO: linearly independent vecs that span the space in question
    # multiple ways of doing this
    return

def transition_matrix(basis_A, basis_B):
    # returns the change-of-coordinates matrix from A to B
    augmented = augment_square(basis_B, basis_A)
    reduced = rref(augmented)
    return disaugment_square(reduced)

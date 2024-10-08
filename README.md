﻿# linearcalc

A library of linear algebra tools written in Python, with an emphasis on avoiding external libraries as much as is possible given the scope of the subject. 

2D lists are to be used as matrices so that some of the functionality provided by numpy is replicated. 

Sympy is to be used for algebraic expressions given that a CAS would constitute a separate and likely more involved project. 

The initial goal is to provide a command line interface, but eventually a UI can be implemented in order to produce something similar to the many linear algebra calculators that can be found online. 

Functionality includes matrix and vector arithmetic, reducing matrices (RREF), determinants, matrix inverses, classifying features of matrices (such as linear independence of constituent vectors), eigenvalues/eigenvectors, similar matrices, orthogonal diagonalization, various forms of factorization (LU, QR), etc.

This project is also providing an opportunity to explore the basics of numerical analysis in relation to floating point precision and propagation of rounding errors. 

This is a side project intended to aid in reinforcement of basic principles of Python programming as well as essential topics of linear algebra. 

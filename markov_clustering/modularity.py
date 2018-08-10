"""
Computation of the modularity of a clustering
"""

import numpy as np
from fractions import Fraction
from itertools import permutations

from scipy.sparse import isspmatrix, dok_matrix, find
from .mcl import sparse_allclose

def is_undirected(matrix):
    """
    Determine if the matrix reprensents a directed graph

    :param matrix: The matrix to tested
    :returns: boolean
    """
    if isspmatrix(matrix):
        return sparse_allclose(matrix, matrix.transpose())
    
    return np.allclose(matrix, matrix.T)


def convert_to_adjacency_matrix(matrix):
    """
    Converts transition matrix into adjacency matrix

    :param matrix: The matrix to be converted
    :returns: adjacency matrix
    """
    for i in range(matrix.shape[0]):
        
        if isspmatrix(matrix):
            col = find(matrix[:,i])[2]
        else:
            col = matrix[:,i].T.tolist()[0]

        coeff = max( Fraction(c).limit_denominator().denominator for c in col )
        matrix[:,i] *= coeff

    return matrix


def delta_matrix(matrix, clusters):
    """
    Compute delta matrix where delta[i,j]=1 if i and j belong
    to same cluster and i!=j
    
    :param matrix: The adjacency matrix
    :param clusters: The clusters returned by get_clusters
    :returns: delta matrix
    """
    if isspmatrix(matrix):
        delta = dok_matrix(matrix.shape)
    else:
        delta = np.zeros(matrix.shape)

    for i in clusters :
        for j in permutations(i, 2):
            delta[j] = 1

    return delta


def modularity(matrix, clusters):
    """
    Compute the modularity

    :param matrix: The adjacency matrix
    :param clusters: The clusters returned by get_clusters
    :returns: modularity value
    """
    matrix = convert_to_adjacency_matrix(matrix)
    m = matrix.sum()

    if isspmatrix(matrix):
        matrix_2 = matrix.tocsr(copy=True)
    else :
        matrix_2 = matrix

    if is_undirected(matrix):
        expected = lambda i,j : (( matrix_2[i,:].sum() + matrix[:,i].sum() )*
                                 ( matrix[:,j].sum() + matrix_2[j,:].sum() ))
    else:
        expected = lambda i,j : ( matrix_2[i,:].sum()*matrix[:,j].sum() )
    
    delta   = delta_matrix(matrix, clusters)
    indices = np.array(delta.nonzero())
    
    Q = sum( matrix[i, j] - expected(i, j)/m for i, j in indices.T )/m
    
    return Q

import pytest
import numpy as np
from scipy.sparse import csc_matrix
import markov_clustering as mc

test_matrices = [
    (   # is undirected
        [[1, 1, 0],
         [0, 1, 1],
         [0, 0, 1]],
        
        False
    ),
    (   # is undirected
        [[1, 0, 0],
         [0, 1, 1],
         [0, 1, 1]],
        
        True
    ),
    (   # convert to adjacency matrix
        [[1, 0.5, 0  ],
         [0, 0.5, 2/3],
         [0,   0, 1/3]],
         
        [[1, 1, 0],
         [0, 1, 2],
         [0, 0, 1]]
    ),
    (   # delta matrix
        [(0,1,2), (3,4,5,6)],
         
        [[0, 1, 1, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 1, 0, 1, 1],
         [0, 0, 0, 1, 1, 0, 1],
         [0, 0, 0, 1, 1, 1, 0]]
    ),
    (   # compute modularity
        [[1/3, 1/3, 1/4, 0  , 0  , 0  , 0  ],
         [1/3, 1/3, 1/4, 0  , 0  , 0  , 0  ],
         [1/3, 1/3, 1/4, 1/4, 0  , 0  , 0  ],
         [0  , 0  , 1/4, 1/4, 1/4, 0  , 1/4],
         [0  , 0  , 0  , 1/4, 1/4, 1/3, 1/4],
         [0  , 0  , 0  , 0  , 1/4, 1/3, 1/4],
         [0  , 0  , 0  , 1/4, 1/4, 1/3, 1/4]],
         
         -284/625
    ),
]

def test_is_undirected_1():
    source = np.matrix(test_matrices[0][0])
    target = test_matrices[0][1]
    
    norm = mc.is_undirected(source)
    assert norm == target


def test_is_undirected_1_sparse():
    source = csc_matrix(test_matrices[0][0])
    target = test_matrices[0][1]
    
    norm = mc.is_undirected(source)
    assert norm == target


def test_is_undirected_2():
    source = np.matrix(test_matrices[1][0])
    target = test_matrices[1][1]
    
    norm = mc.is_undirected(source)
    assert norm == target


def test_is_undirected_2_sparse():
    source = csc_matrix(test_matrices[1][0])
    target = test_matrices[1][1]
    
    norm = mc.is_undirected(source)
    assert norm == target


def test_conversion():
    source = np.matrix(test_matrices[2][0])
    target = np.matrix(test_matrices[2][1])
    
    converted = mc.convert_to_adjacency_matrix(source)
    assert np.array_equal(converted, target)


def test_conversion_sparse():
    source = csc_matrix(test_matrices[2][0])
    target = np.matrix(test_matrices[2][1])
    
    converted = mc.convert_to_adjacency_matrix(source).todense()
    assert np.array_equal(converted, target)


def test_delta_matrix():
    source = test_matrices[3][0]
    target = np.matrix(test_matrices[3][1])
    
    delta = mc.delta_matrix(np.matrix(test_matrices[4][0]), source)
    assert np.array_equal(delta, target)


def test_delta_matrix_sparse():
    source = test_matrices[3][0]
    target = np.matrix(test_matrices[3][1])
    
    delta = mc.delta_matrix( csc_matrix(test_matrices[4][0]), source).todense()
    assert np.array_equal(delta, target)


def test_modularity():
    source = np.matrix(test_matrices[4][0])
    target = test_matrices[4][1]
    clusters = mc.get_clusters(mc.run_mcl(source))

    quality = mc.modularity(source, clusters)
    assert np.isclose(quality, target)


def test_modularity_sparse():
    source = csc_matrix(test_matrices[4][0])
    target = test_matrices[4][1]
    clusters = mc.get_clusters(mc.run_mcl(source))
    
    quality = mc.modularity(source, clusters)
    assert np.isclose(quality, target)

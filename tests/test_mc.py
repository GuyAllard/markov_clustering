import pytest
import numpy as np
import markov_clustering as mc
from scipy.sparse import csc_matrix

test_matrices = [
    (   # normalize
        [[1, 1, 0],
         [0, 1, 1],
         [0, 0, 1]],
        
        [[1, 0.5, 0],
         [0, 0.5, 0.5],
         [0, 0,   0.5]]
    ),
    (   # inflate
        [[0.5, 0.5],
         [1,   1]],
    
        [[0.2, 0.2],
         [0.8, 0.8]]
    ),
    (   # expand
        [[1, 0.5, 0],
         [0, 0.5, 0.5],
         [0, 0, 0.5]],
         
        [[1, 0.75, 0.25],
         [0, 0.25, 0.5 ],
         [0, 0,    0.25]]
    ),
    (   # self loops
        [[0,   0.5, 0],
         [0,   0,   0.5],
         [0.5, 0,   0.5]],
         
        [[2,   0.5, 0],
         [0,   2,   0.5],
         [0.5, 0,   2]]
    ),
    (   # prune
        [[2,   0.5, 0],
         [0,   2,   0.5],
         [0.5, 0,   2]],
    
        [[2, 0, 0],
         [0, 2, 0],
         [0, 0, 2]]
    ),
    # converged
    [[2,   0.5, 0],
     [0,   2,   0.5],
     [0.5, 0,   2]],
    (
        # iterate
        [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]],
    
        [[ 0.44444444,  0.23529412,  0.11111111],
         [ 0.44444444,  0.52941176,  0.44444444],
         [ 0.11111111,  0.23529412,  0.44444444]]
    ),
    (
        # mcl algorithm
        [[1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 1],
         [0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 1, 1, 1, 1]],
         
         [[0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0.],
          [1., 1., 1., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0.5, 0.5, 0.5, 0.5],
          [0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0.5, 0.5, 0.5, 0.5]]
    ),
]

def test_normalize():
    source = np.matrix(test_matrices[0][0])
    target = np.matrix(test_matrices[0][1])
    
    norm = mc.normalize(source)
    assert np.array_equal(norm, target)


def test_normalize_sparse():
    source = csc_matrix(test_matrices[0][0])
    target = np.matrix(test_matrices[0][1])
    
    norm = mc.normalize(source).todense()
    assert np.array_equal(norm, target)


def test_inflate():
    source = np.matrix(test_matrices[1][0])
    target = np.matrix(test_matrices[1][1])
    
    inflated = mc.inflate(source, 2)
    assert np.array_equal(inflated, target)


def test_inflate_sparse():
    source = csc_matrix(test_matrices[1][0])
    target = np.matrix(test_matrices[1][1])
    
    inflated = mc.inflate(source, 2).todense()
    assert np.array_equal(inflated, target)


def test_expand():
    source = np.matrix(test_matrices[2][0])
    target = np.matrix(test_matrices[2][1])
    
    expanded = mc.expand(source, 2)
    assert np.array_equal(expanded, target)


def test_expand_sparse():
    source = csc_matrix(test_matrices[2][0])
    target = np.matrix(test_matrices[2][1])
    
    expanded = mc.expand(source, 2).todense()
    assert np.array_equal(expanded, target)


def test_add_self_loops():
    source = np.matrix(test_matrices[3][0])
    target = np.matrix(test_matrices[3][1])
    
    looped = mc.add_self_loops(source, 2)
    assert np.array_equal(looped, target)


def test_add_self_loops_sparse():
    source = csc_matrix(test_matrices[3][0])
    target = np.matrix(test_matrices[3][1])
    
    looped = mc.add_self_loops(source, 2).todense()
    assert np.array_equal(looped, target)


def test_prune():
    source = np.matrix(test_matrices[4][0])
    target = np.matrix(test_matrices[4][1])
    
    pruned = mc.prune(source, 1)
    assert np.array_equal(pruned, target)


def test_prune_sparse():
    source = csc_matrix(test_matrices[4][0])
    target = np.matrix(test_matrices[4][1])
    
    pruned = mc.prune(source, 1).todense()
    assert np.array_equal(pruned, target)
    
    
def test_converged():
    source = np.matrix(test_matrices[5])
    assert mc.converged(source, source)
    
    source2 = source.copy()
    source2[0,0] = 2.2
    assert not mc.converged(source, source2)


def test_converged_sparse():
    source = csc_matrix(test_matrices[5])
    assert mc.converged(source, source)
    
    source2 = source.copy()
    source2[0,0] = 2.2
    assert not mc.converged(source, source2)
    

def test_iterate():
    source = np.matrix(test_matrices[6][0])
    target = np.matrix(test_matrices[6][1])
    
    iterated = mc.normalize(mc.iterate(source, 2, 2))
    assert np.array_equal(np.round(iterated, 4), np.round(target, 4))


def test_iterate_sparse():
    source = csc_matrix(test_matrices[6][0])
    target = np.matrix(test_matrices[6][1])
    
    iterated = mc.normalize(mc.iterate(source, 2, 2)).todense()
    assert np.array_equal(np.round(iterated, 4), np.round(target, 4))


def test_mcl():
    source = np.matrix(test_matrices[7][0])
    target = np.matrix(test_matrices[7][1])
    
    result = mc.run_mcl(source)
    assert np.array_equal(np.round(result,4), np.round(target, 4))


def test_mcl_sparse():
    source = csc_matrix(test_matrices[7][0])
    target = np.matrix(test_matrices[7][1])
    
    result = mc.run_mcl(source).todense()
    assert np.array_equal(np.round(result, 4), np.round(target, 4))


def test_get_clusters():
    source = np.matrix(test_matrices[7][1])
    target = [(0,1,2), (3,4,5,6)]
    result = mc.get_clusters(source)
    assert result == target


def test_get_clusers_sparse():
    source = csc_matrix(test_matrices[7][1])
    target = [(0,1,2), (3,4,5,6)]
    result = mc.get_clusters(source)
    assert result == target

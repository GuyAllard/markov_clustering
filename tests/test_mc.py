import pytest
import numpy as np
import markov_clustering as mc

def test_normalize_column():
    source = np.matrix([
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
    ])
    
    target = np.matrix([
        [1, 0.5, 0],
        [0, 0.5, 0.5],
        [0, 0,   0.5]
    ])
    
    norm = mc.normalize_columns(source)
    assert np.array_equal(norm, target)


def test_inflate():
    source = np.matrix([
        [0.5, 0.5],
        [1,   1]
    ])
    
    target = np.matrix([
        [0.2, 0.2],
        [0.8, 0.8]
    ])
    
    inflated = mc.inflate(source, 2)
    assert np.array_equal(inflated, target)


def test_expand():
    source = np.matrix([
        [1, 0.5, 0],
        [0, 0.5, 0.5],
        [0, 0, 0.5]
    ])
    
    target = np.matrix([
        [1, 0.75, 0.25],
        [0, 0.25, 0.5 ],
        [0, 0,    0.25]
    ])
    
    expanded = mc.expand(source, 2)
    assert np.array_equal(expanded, target)


def test_add_self_loops():
    source = np.matrix([
        [0,   0.5, 0],
        [0,   0,   0.5],
        [0.5, 0,   0.5]
    ])
    
    target = np.matrix([
        [2,   0.5, 0],
        [0,   2,   0.5],
        [0.5, 0,   2]
    ])
    
    looped = mc.add_self_loops(source, 2)
    assert np.array_equal(looped, target)


def test_prune():
    source = np.matrix([
        [2,   0.5, 0],
        [0,   2,   0.5],
        [0.5, 0,   2]
    ])
    
    target = np.matrix([
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2]
    ])
    
    pruned = mc.prune(source, 1)
    assert np.array_equal(pruned, target)


def test_converged():
    source = np.matrix([
        [2,   0.5, 0],
        [0,   2,   0.5],
        [0.5, 0,   2]
    ])
    
    assert mc.converged(source, source)

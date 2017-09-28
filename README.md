# Markov Clustering

## Implementation of the MCL algorithm in python

The MCL algorithm was developed by Stijn van Dongen at the University of Utrecht.

Details of the algorithm can be found on the [MCL homepage](https://micans.org/mcl/).

### Isn't there already a python module for this?

Yes and no.

There is a module available on pypy called python_mcl which implements this algorithm.
However, reading through the code reveals several issues:
  - Expansion and inflation operations are not performed in the correct order.
  - No support for sparse matrices.
  - No pruning performed.

### This implementation

This module implements the MCL algorithm with support for sparse matrices. The support for sparse
matrices is an important addition as the MCL algorithm is designed for use on graphs whose structure
is inherently sparse. This should allow for clustering of much larger data sets than could be achieved
with dense matrices.

A simple pruning step has been added, the goal of which is to remove very small elements from the
matrix, thereby reducing the number of cells which need to be operated on.


### Installation

TODO


### Usage

TODO 

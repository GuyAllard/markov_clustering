# Markov Clustering

## Implementation of the MCL algorithm in python

The MCL algorithm was developed by Stijn van Dongen at the University of Utrecht.

Details of the algorithm can be found on the [MCL homepage](https://micans.org/mcl/).

### Isn't there already a python module for this?

Yes and no.

There is a module available on pypy called python_mcl which implements this algorithm.
Unfortunately, that module has the following limitations:
- Expansion and inflation operations are not performed in the correct order.
- No support for sparse matrices.
- No pruning performed.

### This implementation

This module implements the MCL algorithm with support for sparse matrices. The support for sparse
matrices is an important addition as the MCL algorithm is designed for use on graphs whose structure
is inherently sparse. This should allow for clustering of larger data sets than could be achieved
with dense matrices.

A simple pruning step has been added, the goal of which is to remove very small elements from the
matrix, thereby further reducing the number of calculations per iteration.


### Requirements

- Core requirements
  - Python 3.x
  - numpy
  - scipy
  - scikit-learn

- Optional (required for visualization)
  - networkx
  - matplotlib 

- To run the tests
  - pytest


### Installation

The recommended installation method is via pip.

To install with all requirements including support for visualization:  
```
pip install markov_clustering[drawing]
```

To install with only support for the core MCL clustering:  
```
pip install markov_clustering
```


### Example

![example visualization](/static/example.png)

We will use NetworkX to generate the adjacency matrix for a random geometric graph which contains 200 nodes
with random coordinates ranging from (-1,-1) to (1,1). Nodes are considered adjacent if the distance between 
them is <= 0.3 units.  

This example assumes that the optional dependencies (matplotlib and networkx) have been installed

```python
import markov_clustering as mc
import networkx as nx
import random

# number of nodes to use
numnodes = 200

# generate random positions as a dictionary where the key is the node id and the value
# is a tuple containing 2D coordinates
positions = {i:(random.random() * 2 - 1, random.random() * 2 - 1) for i in range(numnodes)}

# use networkx to generate the graph
network = nx.random_geometric_graph(numnodes, 0.3, pos=positions)

# then get the adjacency matrix (in sparse form)
matrix = nx.to_scipy_sparse_matrix(network)
```

We can then run the MCL algorithm on the adjacency matrix and retrieve the clusters.
```python
result = mc.run_mcl(matrix)           # run MCL with default parameters
clusters = mc.get_clusters(result)    # get clusters
```

Finally, we can draw the results. The draw_graph function only requires the adjacency matrix and the 
cluster list, but we will pass some extra parameters such as the node positions, set the node size,
disable labels and set the color for edges.
```python
mc.draw_graph(matrix, clusters, pos=positions, node_size=50, with_labels=False, edge_color="silver")
```
This should result in an image similar to the one at the top of this section. 


If the clustering is too fine for your taste, reducing the MCL inflation parameter to 1.4 (from the default of 2)
will result in coarser clustering. e.g.
```
result = mc.run_mcl(matrix, inflation=1.4)
clusters = mc.get_clusters(result)
mc.draw_graph(matrix, clusters, pos=positions, node_size=50, with_labels=False, edge_color="silver")
```
![coarse example](/static/example_coarse.png)

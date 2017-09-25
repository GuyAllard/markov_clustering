# Markov Clustering

## Implementation of the MCL algorithm in python

The MCL algorithm was developed by Stijn van Dongen at the University of Utrecht.

Details of the algorithm can be found in the thesis [Graph Clustering by Flow Simulation](http://www.library.uu.nl/digiarchief/dip/diss/1895620/inhoud.htm).

### Isn't there already a python module for this?

Yes and no.

There is a module available on pypy called python_mcl which implements this algorithm.
However, reading through the code reveals that the expansion and inflation operations are not performed in the correct order.
 

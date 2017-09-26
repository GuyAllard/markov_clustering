import numpy as np

graph = np.matrix([
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]
])

def normalize_columns(matrix):
    """
    Normalize the columns of the given matrix
    
    :param matrix: A numpy matrix
    :returns: The normalized matrix
    """
    col_sums = np.linalg.norm(matrix, ord=1, axis=0)
    return matrix / col_sums


def inflate(matrix, power):
    """
    Apply cluster inflation to the given matrix
    
    :param matrix: A numpy matrix
    :param power: Cluster inflation parameter
    :returns: The inflated matrix
    """
    return normalize_columns(np.power(matrix, power))


def expand(matrix, power):
    """
    Apply cluster expansion to the given matrix
    
    :param matrix: A numpy matrix
    :param power: Cluster expansion parameter
    :returns: The expanded matrix
    """
    return np.linalg.matrix_power(matrix, power)


def add_self_loops(matrix, loop_value):
    """
    Add self-loops to the matrix by setting the diagonal
    to loop_value
    
    :param matrix: A numpy matrix
    :param loop_value: Value to use for self-loops
    :returns: The matrix with self-loops
    """
    shape = matrix.shape
    assert shape[0] == shape[1], "Error, matrix is not square"
    
    new_matrix = matrix.copy()
    for i in range(shape[0]):
        new_matrix[i, i] = loop_value
    
    return new_matrix


def prune(matrix, threshold):
    """
    Prune the matrix so that very small edges are removed
    
    :param matrix: A numpy matrix
    :param threshold: The value below which edges will be removed
    :returns: The pruned matrix
    """
    pruned = matrix.copy()
    pruned[pruned < threshold] = 0
    return pruned


def converged(matrix1, matrix2):
    """
    Are matrix1 and matrix2 approximately equal?
    
    :param matrix1: A numpy matrix
    :param matrix2: A numpy matrix
    :param tolerance: Threshold for determining equality
    :returns: True if matrix1 and matrix2 approximately equal
    """
    return np.allclose(matrix1, matrix2) 


def run_mcl(matrix, expansion=2, inflation=2, loop_value=1,
            iterations=10, pruning=0.001, verbose=False):
    """
    Perform MCL on the given similarity matrix
    
    :param matrix: The similarity matrix to cluster
    :param expansion: The cluster expansion factor
    :param inflation: The cluster inflation factor
    :param loop_value: Initialization value for self-loops
    :param iterations: Maximum number of iterations
                       (actual number of iterations will be less if
                        convergence is reached)
    :param pruning: Threshold below which matrix elements will be set
                    set to 0
    :param verbose: Print extra information to the console
    """
    # Step 1: Initialize self-loops
    matrix = add_self_loops(matrix, loop_value)
    
    # Step 2: Normalize
    matrix = normalize_columns(matrix)
    
    for i in range(iterations):
        # store current matrix for convergence checking
        last_mat = matrix.copy()
        
        # Step 3: Expansion
        matrix = expand(matrix, expansion)
  
        # Step 4: Inflation
        matrix = inflate(matrix, inflation)
        
        # Step 5: Pruning (should be optional)
        matrix = prune(matrix, pruning)
        
        if verbose:
            print(matrix)
        
        # Step 6: Check for convergence
        if converged(matrix, last_mat):
            print("Converged after {} iterations".format(i))
            break
   
    print(matrix)

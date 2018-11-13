"""
Visualization of clusters
"""
import sys

try:
    import networkx as nx
except ImportError:
    sys.stderr.write("Networkx not present\n")
    raise
    
try:
    from matplotlib.pylab import show, cm, axis
except ImportError:
    sys.stderr.write("Matplotlib not present\n")
    raise


def draw_graph(matrix, clusters, **kwargs):
    """
    Visualize the clustering
    
    :param matrix: The unprocessed adjacency matrix
    :param clusters: list of tuples containing clusters as returned
                     by 'get_clusters'
    :param kwargs: Additional keyword arguments to be passed to
                   networkx.draw_networkx
    """
    # make a networkx graph from the adjacency matrix
    graph = nx.Graph(matrix)
    
    # map node to cluster id for colors
    cluster_map = {node: i for i, cluster in enumerate(clusters) for node in cluster}
    colors = [cluster_map[i] for i in range(len(graph.nodes()))]
    
    # if colormap not specified in kwargs, use a default
    if not kwargs.get("cmap", False):
        kwargs["cmap"] = cm.tab20
    
    # draw
    nx.draw_networkx(graph, node_color=colors, **kwargs)
    axis("off")
    show(block=False)

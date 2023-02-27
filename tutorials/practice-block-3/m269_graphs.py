
EMPTY = UndirectedGraph()

def null_graph(n: int) -> UndirectedGraph:
    """Return a graph with nodes 0, 1, ..., n-1 and no edges.

    Preconditions: n > 0
    """
    graph = UndirectedGraph()
    for node in range(n):
        graph.add_node(node)
    return graph

def path_graph(n: int) -> UndirectedGraph:
    """Return a graph with nodes 0, ..., n-1 and edges 0–1, 1–2, ....

    Preconditions: n > 0
    """
    graph = null_graph(n)
    for node in range(n-1):
        graph.add_edge(node, node+1)
    return graph

def cycle_graph(n: int) -> UndirectedGraph:
    """Return a graph with nodes 0, ..., n-1 and edges 0–1, 1–2, ..., (n-1)–0.

    Preconditions: n > 0
    """
    graph = path_graph(n)
    graph.add_edge(n-1, 0)
    return graph

def complete_graph(n: int) -> UndirectedGraph:
    """Return a graph with nodes 0, ..., n-1 connected to each other.

    Preconditions: n > 0
    """
    graph = null_graph(n)
    for node1 in range(n):
        for node2 in range(node1 + 1, n):
            graph.add_edge(node1, node2)
    return graph

from random import random

def random_graph(n: int, probability: float) -> UndirectedGraph:
    """Generate a random graph with n nodes.

    Each edge has the given probability of existing.
    Preconditions: 0 <= probability <= 1
    """
    graph = null_graph(n)
    for node1 in range(n):
        for node2 in range(node1 + 1, n):
            if random() < probability:
                graph.add_edge(node1, node2)
    return graph

# graph in the figure above
RHOMBUS = WeightedUndirectedGraph()
for node in 'ABCD':
    RHOMBUS.add_node(node)
for edge in ('AB1', 'AD2', 'BC4', 'BD2', 'CD5'):
    RHOMBUS.add_edge(edge[0], edge[1], int(edge[2]))

# graph used by the interactive visualisation of Dijkstra's algorithm
DIJKSTRA = WeightedUndirectedGraph()
for node in 'ABCDEFGHK':
    DIJKSTRA.add_node(node)
for edge in ('AB4','BF1','BG3','CD2','DE2','EG3','EK3','FH1','GK5','HK3'):
    DIJKSTRA.add_edge(edge[0], edge[1], int(edge[2]))
DIJKSTRA.add_edge('A', 'C', 20)

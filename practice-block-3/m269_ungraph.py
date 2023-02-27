from m269_digraph import DiGraph
from m269_digraph import WeightedDiGraph

from typing import Hashable

class UndirectedGraph(DiGraph):
    """An undirected graph with hashable node objects.

    There's at most one edge between two different nodes.
    There are no edges between a node and itself.
    """

    def add_edge(self, node1: Hashable, node2: Hashable) -> None:
        """Add an undirected edge node1-node2 to the graph.

        If the edge already exists, do nothing.

        Preconditions: self.has_node(node1) and self.has_node(node2)
        """
        super().add_edge(node1, node2)
        super().add_edge(node2, node1)

    def remove_edge(self, node1: Hashable, node2: Hashable) -> None:
        """Remove edge node1-node2 from the graph.

        If the edge doesn't exist, do nothing.

        Preconditions: self.has_node(node1) and self.has_node(node2)
        """
        super().remove_edge(node1, node2)
        super().remove_edge(node2, node1)

    def edges(self) -> set:
        """Return the graph's edges as a set of pairs.

        Postconditions: for every edge A-B,
        the output has either (A, B) or (B, A) but not both
        """
        all_edges = set()
        for node1 in self.out:
            for node2 in self.out[node1]:
                if (node2, node1) not in all_edges:
                    all_edges.add( (node1, node2) )
        return all_edges

    def in_neighbours(self, node: Hashable) -> set:
        """Return all nodes that are adjacent to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_neighbours(node)

    def neighbours(self, node: Hashable) -> set:
        """Return all nodes that are adjacent to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_neighbours(node)

    def in_degree(self, node: Hashable) -> int:
        """Return the number of edges attached to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_degree(node)

    def degree(self, node: Hashable) -> int:
        """Return the number of edges attached to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_degree(node)

class WeightedUndirectedGraph(WeightedDiGraph):
    """A weighted undirected graph with hashable node objects.

    There's at most one edge between two different nodes.
    There are no edges between a node and itself.
    Edges have weights, which may be integers or floats.
    """

    def add_edge(self, node1: Hashable, node2: Hashable, weight: float) -> None:
        """Add an edge node1-node2 with the given weight to the graph.

        If the edge already exists, do nothing.

        Preconditions: self.has_node(node1) and self.has_node(node2)
        """
        super().add_edge(node1, node2, weight)
        super().add_edge(node2, node1, weight)

    def remove_edge(self, node1: Hashable, node2: Hashable) -> None:
        """Remove edge node1-node2 from the graph.

        If the edge doesn't exist, do nothing.

        Preconditions: self.has_node(node1) and self.has_node(node2)
        """
        super().remove_edge(node1, node2)
        super().remove_edge(node2, node1)

    def edges(self) -> set:
        """Return the graph's edges as a set of triples (node1, node2, weight).

        Postconditions: for every edge A-B,
        the output has either (A, B, w) or (B, A, w) but not both
        """
        all_edges = set()
        for start in self.out:
            for (end, weight) in self.out[start].items():
                if (end, start, weight) not in all_edges:
                    all_edges.add( (start, end, weight) )
        return all_edges

    def in_neighbours(self, node: Hashable) -> set:
        """Return all nodes that are adjacent to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_neighbours(node)

    def neighbours(self, node: Hashable) -> set:
        """Return all nodes that are adjacent to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_neighbours(node)

    def in_degree(self, node: Hashable) -> int:
        """Return the number of edges attached to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_degree(node)

    def degree(self, node: Hashable) -> int:
        """Return the number of edges attached to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_degree(node)

from heapq import heappush, heappop

def prim(graph: WeightedUndirectedGraph, start: Hashable) -> WeightedUndirectedGraph:
    """Return a minimum spanning tree of graph, beginning at start.

    Preconditions:
    - graph.has_node(start)
    - graph is connected
    - node objects are comparable
    """
    visited = WeightedUndirectedGraph()
    visited.add_node(start)

    unprocessed = []
    for neighbour in graph.neighbours(start):
        weight = graph.weight(start, neighbour)
        heappush(unprocessed, (weight, start, neighbour) )

    while len(unprocessed) > 0:
        edge = heappop(unprocessed)
        weight = edge[0]
        previous = edge[1]
        current = edge[2]
        if not visited.has_node(current):
            visited.add_node(current)
            visited.add_edge(previous, current, weight)
            for neighbour in graph.neighbours(current):
                weight = graph.weight(current, neighbour)
                heappush(unprocessed, (weight, current, neighbour) )
    return visited

def connected_components(graph: UndirectedGraph) -> dict:
    """Return the connected components of graph.

    Postconditions: the output maps each node to its component,
    numbered from 1 onwards.
    """
    component = dict()
    counter = 1
    for node in graph.nodes():
        if node not in component:
            tree = dfs(graph, node)
            for reached in tree.nodes():
                component[reached] = counter
            counter = counter + 1
    return component

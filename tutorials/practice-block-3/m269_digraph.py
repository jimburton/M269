
import networkx
from typing import Hashable

class DiGraph:
    """A directed graph with hashable node objects.

    Edges are between different nodes.
    There's at most one edge from one node to another.
    """

    def __init__(self):
        self.out = dict()   # a map of nodes to their out-neighbours

    def has_node(self, node: Hashable) -> bool:
        """Return True if and only if the graph has the node."""
        return node in self.out

    def has_edge(self, start: Hashable, end: Hashable) -> bool:
        """Return True if and only if edge start -> end exists.

        Preconditions: self.has_node(start) and self.has_node(end)
        """
        return end in self.out[start]

    def add_node(self, node: Hashable) -> None:
        """Add the node to the graph.

        Preconditions: not self.has_node(node)
        """
        self.out[node] = set()

    def add_edge(self, start: Hashable, end: Hashable) -> None:
        """Add edge start -> end to the graph.

        If the edge already exists, do nothing.

        Preconditions:
        self.has_node(start) and self.has_node(end) and start != end
        """
        self.out[start].add(end)

    def remove_node(self, node: Hashable) -> None:
        """Remove the node and all its attached edges.

        Preconditions: self.has_node(node)
        """
        for start in self.out:
            self.remove_edge(start, node)
        self.out.pop(node)

    def remove_edge(self, start: Hashable, end: Hashable) -> None:
        """Remove edge start -> end from the graph.

        If the edge doesn't exist, do nothing.

        Preconditions: self.has_node(start) and self.has_node(end)
        """
        self.out[start].discard(end)

    def nodes(self) -> set:
        """Return the graph's nodes."""
        all_nodes = set()
        for node in self.out:
            all_nodes.add(node)
        return all_nodes

    def edges(self) -> set:
        """Return the graph's edges as a set of pairs (start, end)."""
        all_edges = set()
        for start in self.out:
            for end in self.out[start]:
                all_edges.add( (start, end) )
        return all_edges

    def out_neighbours(self, node: Hashable) -> set:
        """Return the out-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        return set(self.out[node])  # return a copy

    def out_degree(self, node: Hashable) -> int:
        """Return the number of out-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        return len(self.out[node])

    def in_neighbours(self, node: Hashable) -> set:
        """Return the in-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        start_nodes = set()
        for start in self.out:
            if self.has_edge(start, node):
                start_nodes.add(start)
        return start_nodes

    def in_degree(self, node: Hashable) -> int:
        """Return the number of in-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        return len(self.in_neighbours(node))

    def neighbours(self, node: Hashable) -> set:
        """Return the in- and out-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        return self.out_neighbours(node).union(self.in_neighbours(node))

    def degree(self, node: Hashable) -> int:
        """Return the number of in- and out-going edges of the node.

        Preconditions: self.has_node(node)
        """
        return self.in_degree(node) + self.out_degree(node)

    def draw(self) -> None:
        """Draw the graph."""
        if type(self) == DiGraph:
            graph = networkx.DiGraph()
        else:
            graph = networkx.Graph()
        graph.add_nodes_from(self.nodes())
        graph.add_edges_from(self.edges())
        networkx.draw(graph, with_labels=True,
            node_size=1000, node_color='lightblue',
            font_size=12, font_weight='bold')

from collections import deque

def bfs(graph: DiGraph, start: Hashable) -> DiGraph:
    """Return the subgraph traversed by a breadth-first search.

    Preconditions: graph.has_node(start)
    """
    # changes from traversed function noted in comments
    visited = DiGraph()
    visited.add_node(start)
    unprocessed = deque()                           # set -> deque
    for neighbour in graph.out_neighbours(start):
        unprocessed.append( (start, neighbour) )    # add -> append
    while len(unprocessed) > 0:
        edge = unprocessed.popleft()                # pop -> popleft
        previous = edge[0]
        current = edge[1]
        if not visited.has_node(current):
            visited.add_node(current)
            visited.add_edge(previous, current)
            for neighbour in graph.out_neighbours(current):
                unprocessed.append( (current, neighbour) )  # add -> append
    return visited

def dfs(graph: DiGraph, start: Hashable) -> DiGraph:
    """Return the subgraph traversed by a depth-first search.

    Preconditions: graph.has_node(start)
    """
    visited = DiGraph()
    visited.add_node(start)
    unprocessed = []                            # deque -> list
    for neighbour in graph.out_neighbours(start):
        unprocessed.append( (start, neighbour) )
    while len(unprocessed) > 0:
        edge = unprocessed.pop()                # popleft -> pop
        previous = edge[0]
        current = edge[1]
        if not visited.has_node(current):
            visited.add_node(current)
            visited.add_edge(previous, current)
            for neighbour in graph.out_neighbours(current):
                unprocessed.append( (current, neighbour) )
    return visited

import math

class WeightedDiGraph(DiGraph):
    """A weighted directed graph with hashable node objects.

    Edges are between different nodes.
    There's at most one edge from one node to another.
    Edges have weights, which can be floats or integers.
    """

    def add_node(self, node: Hashable) -> None:
        """Add the node to the graph.

        Preconditions: not self.has_node(node)
        """
        self.out[node] = dict() # a map of out-neighbours to weights

    def add_edge(self, start: Hashable, end: Hashable, weight: float) -> None:
        """Add edge start -> end, with the given weight, to the graph.

        If the edge already exists, set its weight.

        Preconditions:
        self.has_node(start) and self.has_node(end) and start != end
        """
        self.out[start][end] = weight

    def weight(self, start: Hashable, end: Hashable) -> float:
        """Return the weight of edge start -> end or infinity if it doesn't exist.

        Preconditions: self.has_node(start) and self.has_node(end)
        """
        if self.has_edge(start, end):
            return self.out[start][end]
        else:
            return math.inf

    def remove_edge(self, start: Hashable, end: Hashable) -> None:
        """Remove edge start -> end from the graph.

        If the edge doesn't exist, do nothing.

        Preconditions: self.has_node(start) and self.has_node(end)
        """
        if self.has_edge(start, end):
            self.out[start].pop(end)

    def edges(self) -> set:
        """Return the graph's edges as a set of triples (start, end, weight)."""
        all_edges = set()
        for start in self.out:
            for (end, weight) in self.out[start].items():
                all_edges.add( (start, end, weight) )
        return all_edges

    def out_neighbours(self, node: Hashable) -> set:
        """Return the out-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        return set(self.out[node].keys())

    def draw(self) -> None:
        """Draw the graph."""
        if type(self) == WeightedDiGraph:
            graph = networkx.DiGraph()
        else:
            graph = networkx.Graph()
        graph.add_nodes_from(self.nodes())
        for (node1, node2, weight) in self.edges():
            graph.add_edge(node1, node2, w=weight)
        pos = networkx.spring_layout(graph)
        networkx.draw(graph, pos, with_labels=True,
            node_size=1000, node_color='lightblue',
            font_size=12, font_weight='bold')
        networkx.draw_networkx_edge_labels(graph, pos,
            edge_labels=networkx.get_edge_attributes(graph, 'w'))

from heapq import heappush, heappop

def dijkstra(graph: WeightedDiGraph, start: Hashable) -> WeightedDiGraph:
    """Return a shortest path from start to each reachable node.

    Preconditions:
    - graph.has_node(start)
    - node objects are comparable
    - no weight is negative
    """
    visited = WeightedDiGraph()
    visited.add_node(start)

    # create min-priority queue of tuples (cost, (A, B, weight))
    # cost is total weight from start to B via shortest path to A
    unprocessed = []    # min-priority queue
    for neighbour in graph.out_neighbours(start):
        weight = graph.weight(start, neighbour)
        heappush(unprocessed, (weight, (start, neighbour, weight)) )

    while len(unprocessed) > 0:
        info = heappop(unprocessed)
        cost = info[0]
        edge = info[1]
        previous = edge[0]
        current = edge[1]
        weight = edge[2]

        if not visited.has_node(current):
            visited.add_node(current)
            visited.add_edge(previous, current, weight)
            for neighbour in graph.out_neighbours(current):
                weight = graph.weight(current, neighbour)
                edge = (current, neighbour, weight)
                heappush(unprocessed, (cost + weight, edge) )
    return visited

def reverse(graph: DiGraph) -> DiGraph:
    """Return the same graph but with edge directions reversed."""
    reversed = DiGraph()
    for node in graph.nodes():
        reversed.add_node(node)
    for edge in graph.edges():
        reversed.add_edge(edge[1], edge[0])
    return reversed

def strongly_connected_components(graph: DiGraph) -> dict:
    """Return the strongly connected components of graph.

    Postconditions: the output maps each node to its component,
    numbered from 1 onwards.
    """
    reversed = reverse(graph)
    component = dict()
    counter = 1
    for node in graph.nodes():
        if node not in component:
            forward = dfs(graph, node).nodes()
            backward = dfs(reversed, node).nodes()
            for common in forward.intersection(backward):
                component[common] = counter
            counter = counter + 1
    return component

def topological_sort(graph: DiGraph) -> list:
    """Return a topological sort of graph.

    Preconditions: graph is acyclic
    Postconditions:
    - the output is a permutation of the graph's nodes
    - for every edge A -> B, node A appears before B in the output
    """
    schedule = []

    # compute the initial in-degrees
    indegree = dict()
    for node in graph.nodes():
        indegree[node] = 0
    for edge in graph.edges():
        indegree[edge[1]] = indegree[edge[1]] + 1

    # compute the nodes that can be visited first
    to_visit = []               # use a list as a stack
    for node in graph.nodes():
        if indegree[node] == 0:
            to_visit.append(node)

    while len(to_visit) > 0:
        visited = to_visit.pop()
        schedule.append(visited)
        # simulate the removal of the visited node
        for neighbour in graph.neighbours(visited):
            indegree[neighbour] = indegree[neighbour] - 1
            if indegree[neighbour] == 0:
                to_visit.append(neighbour)
    return schedule

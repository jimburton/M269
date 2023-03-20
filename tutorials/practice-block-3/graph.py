class Graph:
    """
    A simple directed graph datatype. Nodes (vertices) are stored as a set.
    Edges are stored as a set of pairs of nodes. Self-referential nodes
    (i.e. an edge (n,n)) are allowed. Because nodes and edges aren't stored
    in a more efficient data structure (such as a dict) this is quite
    inefficient but a good way to understand what's going on.
    """

    def __init__(self):
        """
        Construct a new empty graph.
        """
        self.nodes = set()
        self.edges = set()

    @classmethod
    def build(cls, ns: set, es: set):
        """
        Convenience method for constructing a graph from sets of nodes and
        edges. Nodes may be values of any type. Edges must be tuples,
        otherwise a RuntimeError is thrown.
        """
        g = Graph()
        g.nodes = ns
        for e in es:
            if isinstance(e, tuple):
                g.add_edge(e)
            else:
                raise RuntimeError(f"Not a tuple of nodes: {e}")
        return g

    def add_node(self, n) -> None:
        """
        Adds a node to the graph.
        """
        if n not in self.nodes:
            self.nodes.add(n)

    def add_edge(self, e) -> None:
        """
        Adds an edge to the graph. Inconsistencies in the edges (eg either
        element of the tuple is not in the graph) will cause a RuntimeError.
        """
        if e[0] not in self.nodes or e[1] not in self.nodes:
            raise RuntimeError(f"One or both nodes not in graph: {e}")
        if e not in self.edges:
            self.edges.add(e)

    def disconnected(self) -> set:
        """
        Collects the set of disconnected nodes (those which are not part
        of any edge) in the graph.
        """
        return set()

    def elem(self, n) -> bool:
        """
        Returns true if n is a node in this graph, otherwise false.
        """
        return False

    def neighbours_out(self, n) -> set:
        """
        The set of nodes that are connected to n by an edge, where n is the
        source of that edge.

        Throws a RuntimeError if n is not in the graph. 
        """
        return set()

    def neighbours_in(self, n) -> set:
        """
        The set of nodes that are connected to n by an edge, where n is the
        target of that edge.

        Throws a RuntimeError if n is not in the graph. 
        """
        return set()

    def traverse_df_rec(self, n) -> list:
        """
        Performs a recursive depth-first traversal of the graph starting at
        n, and returns the node labels into a list.

        Throws a RuntimeError if n is not in the graph. 
        """
        return []

    def traverse_df_iter(self, n) -> list:
        """
        Performs an iterative depth-first traversal of the graph starting at
        n, and returns the node labels into a list. Here we are using a plain
        old list as a stack.

        Throws a RuntimeError if n is not in the graph.
        """
        return []
        
    def traverse_bf(self, n) -> list:
        """
        Performs an iterative breadth-first traversal of the graph starting at
        n, and returns the node labels into a list. Here we are using a plain old
        list as a queue.

        Throws a RuntimeError if n is not in the graph.
        """
        return []

        def __str__(self):
            """
            Format a graph for display in the REPL.
            """
            return f"({self.nodes}, {self.edges})"

# End of the Graph class
    
# a couple of trees for playing in the REPL
                    
tree0 = Graph.build({'A', 'B', 'C', 'D'},     # nodes
                    {('A', 'B'), ('A', 'C')}) # edges

tree1 = Graph.build({'A', 'B', 'C', 'D', 'E', 'F', 'G'}     # nodes
                    , {('A', 'B'), ('A', 'C'), ('A', 'E')   # edges
                       , ('B', 'D'), ('B', 'F'), ('C', 'G')
                       , ('E', 'F')})

tree_discon = Graph.build({'A', 'B', 'C', 'D', 'E', 'F', 'G'}     # nodes
                    , {('A', 'C'), ('A', 'F')})

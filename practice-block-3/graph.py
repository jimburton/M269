class Graph:
    """A simple directed graph datatype. """

    def __init__(self):
        self.nodes = set()
        self.edges = set()

    @classmethod
    def build(cls, ns: set, es: set):
        g = Graph()
        g.nodes = ns
        for e in es:
            if isinstance(e, tuple):
                if e[0] in ns and e[1] in ns:
                    g.add_edge(e)
                else:
                    raise RuntimeError(f"One or both nodes not in graph: {e}")
            else:
                raise RuntimeError(f"Not a tuple of nodes: {e}")
        return g

    def add_vertex(self, v) -> None:
        if v not in self.nodes:
            self.nodes.add(v)

    def add_edge(self, e) -> None:
        if e[0] not in self.nodes or e[1] not in self.nodes:
            raise RuntimeError(f"One or both nodes not in graph: {e}")
        if e not in self.edges:
            self.edges.add(e)

    def __str__(self):
        return f"({self.nodes}, {self.edges})"

    def disconnected(self) -> set:
        result = self.nodes.copy()
        for n in self.nodes:
            for e in self.edges:
                if n == e[0] or n == e[1]:
                    result.discard(n)
        return result

    def neighbours_out(self, node) -> set:
        if node not in self.nodes:
            raise RuntimeError(f"Node not in graph: {node}")
        result = set()
        for e in self.edges:
            if e[0] == node:
                result.add(e[1])
        return result

    def neighbours_in(self, node) -> set:
        if node not in self.nodes:
            raise RuntimeError(f"Node not in graph: {node}")
        result = set()
        for e in self.edges:
            if e[1] == node:
                result.add(e[0])
        return result

    def traverse_df(self, node) -> list:
        """
        procedure DFS(G, v) is
    label v as discovered
    for all directed edges from v to w that are in G.neighbours(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
        """
        if node not in self.nodes:
            raise RuntimeError(f"Node not in graph: {node}")
        result = [node]
        for n in self.neighbours_out(node):
            result.extend(self.traverse_df(n))
        return list(dict.fromkeys(result))

    def traverse_bf(self, node) -> list:
        """
        Input: A graph G and a starting vertex root of G

Output: Goal state. The parent links trace the shortest path back to root[8]

 1  procedure BFS(G, root) is
 2      let Q be a queue
 3      label root as explored
 4      Q.enqueue(root)
 5      while Q is not empty do
 6          v := Q.dequeue()
 7          if v is the goal then
 8              return v
 9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as explored then
11                  label w as explored
12                  w.parent := v
13                  Q.enqueue(w)
        """
        if node not in self.nodes:
            raise RuntimeError(f"Node not in graph: {node}")
        queue = [node]
        result = [node]
        while queue:
            n = queue.pop(0)
            for n in self.neighbours_out(n):
                if n not in result:
                    result.append(n)
                    queue.append(n)
        return result
                    


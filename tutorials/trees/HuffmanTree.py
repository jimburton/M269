from Tree import *

class HuffmanTree(Tree):
    """Nodes for a Huffman tree. The expectation is that branch nodes
    are labelled by an int, which is the combined frequency counts of the left
     and right subtrees, whereas leaf nodes are labelled by a pair of
    a character and its frequency."""

    def get_frequency(self) -> int:
        """Get the frequency count from a node."""
        return self.value if not self.is_leaf else self.value[1]
    
    def __lt__(self, other: 'HuffmanTree') -> bool:
        return self.get_frequency() < other.get_frequency()
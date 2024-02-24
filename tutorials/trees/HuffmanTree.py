from Tree import *

class HuffmanTree(Tree):

    def get_frequency(self) -> int:
        """Get the frequency count from a node. If the node is a branch node, 
        self.value is its frequency count. If it is a leaf node, self.value is 
        a tuple of the char and its frequency."""
        return self.value if not self.is_leaf else self.value[1]
    
    def __lt__(self, other: 'HuffmanTree') -> bool:
        return self.get_frequency() < other.get_frequency()
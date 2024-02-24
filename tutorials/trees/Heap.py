import math
from Tree import *

class MinHeap:
    """A min heap that stores instances of the Tree class for use in a
    Huffman coding.
    """

    def __init__(self) -> None:
        self.heap = []

    def size(self):
        """Get the size of the heap."""
        return len(self.heap)
    
    def get_frequency(self, t: Tree) -> int:
        """Get the frequency count from a node. If the node is a branch node, 
        self.value is its frequency count. If it is a leaf node, self.value is 
        a tuple of the char and its frequency."""
        return t.value if not t.is_leaf else t.value[1]

    def insert(self, item: Tree) -> None:
        """Insert a node to the heap."""
        pass

    def remove(self) -> Tree:
        """Remove the first node from the heap."""
        pass

    def trickle_up(self) -> None:
        """Swap the last item in the heap with its parent until
        the heap property holds.
        """
        pass
            

    def trickle_down(self) -> None:
        """Swap the first item in the heap with one of its children
        until the heap property holds.
        """
        pass

    def left_child(self, i: int) -> int:
        """Calculate the index of the left hand child of the node stored at i."""
        return 2*i + 1

    def right_child(self, i: int) -> int:
        """Calculate the index of the right hand child of the node stored at i."""
        return 2*i + 2

    def parent(self, i: int) -> int:
        """Calculate the index of the parent of the node stored at i."""
        return math.floor((i-1)/2)

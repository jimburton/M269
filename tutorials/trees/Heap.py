from Tree import *

class MinHeap:
    """A min heap that stores instances of the Tree class for use in a
    Huffman coding. If a Tree object is a branch node, use self.value to 
    get its frequency count. If it is a leaf node, self.value is a tuple 
    of the char and its frequency.
    """

    def __init__(self) -> None:
        self.heap = []

    def insert(self, item: Tree) -> None:
        pass

    def remove(self) -> Tree:
        pass

    def trickle_up(self) -> None:
        pass

    def trickle_down(self) -> None:
        pass

    def left_child(i: int) -> int:
        return 2*i + 1

    def right_child(i: int) -> int:
        return 2*i + 2

    def parent(i: int) -> int:
        return round((i-1)/2)
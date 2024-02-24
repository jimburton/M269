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
        self.heap.append(item)
        self.trickle_up()

    def remove(self) -> Tree:
        """Remove the first node from the heap."""
        if len(self.heap) == 0:
            return None
        else:
            result = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.trickle_down()
            return result

    def trickle_up(self) -> None:
        """Swap the last item in the heap with its parent until
        the heap property holds.
        """
        pos = len(self.heap)-1
        t = self.heap[pos]
        pos_parent = self.parent(pos)
        t_p = self.heap[pos_parent]
        while self.get_frequency(t) < self.get_frequency(t_p) and pos > 0:
            self.heap[pos],self.heap[pos_parent] = self.heap[pos_parent],self.heap[pos]
            pos = pos_parent
            pos_parent = self.parent(pos)
            t_p = self.heap[pos_parent]
            

    def trickle_down(self) -> None:
        """Swap the first item in the heap with one of its children
        until the heap property holds.
        """
        pos = 0
        count = len(self.heap)
        if pos < count:
            done = False
            while not done:
                t = self.heap[pos] 
                t_freq = self.get_frequency(t)
                pos_l = self.left_child(pos)
                pos_r = self.right_child(pos)
                if pos_r < count:
                    t_l = self.heap[pos_l]
                    t_r = self.heap[pos_r]
                    f_l = self.get_frequency(t_l)
                    f_r = self.get_frequency(t_r)
                    if f_l < t_freq or f_r < t_freq:
                        dest = pos_l if f_l < f_r else pos_r
                        self.heap[pos],self.heap[dest] = self.heap[dest],self.heap[pos]
                        pos = dest
                    else:
                        done = True
                elif pos_l < count:
                    t_l = self.heap[pos_l]
                    f_l = self.get_frequency(t_l)
                    if f_l < t_freq:
                        self.heap[pos],self.heap[pos_l] = self.heap[pos_l],self.heap[pos]
                        pos = pos_l
                    else:
                        done = True
                else:
                    done = True

    def left_child(self, i: int) -> int:
        """Calculate the index of the left hand child of the node stored at i."""
        return 2*i + 1

    def right_child(self, i: int) -> int:
        """Calculate the index of the right hand child of the node stored at i."""
        return 2*i + 2

    def parent(self, i: int) -> int:
        """Calculate the index of the parent of the node stored at i."""
        return math.floor((i-1)/2)

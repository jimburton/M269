import math
from enum import Enum
from typing import Any

class Heap:
    """A heap that can be min or max. Values stored must be capable of comparison
    with (<) and (>).
    """
    Direction = Enum('Direction', ['ASC', 'DESC'])

    def __init__(self, dir: Direction) -> None:
        self.heap = []
        self.dir = dir
        self.__cmp = self.__lt if dir.name == 'ASC' else self.__gt

    def __lt(self, x, y):
        return x < y
    
    def __gt(self, x, y):
        return x > y

    def size(self):
        """Get the size of the heap."""
        return len(self.heap)

    def insert(self, item: Any) -> None:
        """Insert a node to the heap."""
        self.heap.append(item)
        self.__trickle_up()

    def remove(self) -> Any:
        """Remove the first node from the heap."""
        if len(self.heap) == 0:
            return None
        else:
            result = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.__trickle_down()
            return result

    def __trickle_up(self) -> None:
        """Swap the last item in the heap with its parent until
        the heap property holds.
        """
        pos = len(self.heap)-1
        t = self.heap[pos]
        pos_parent = self.parent(pos)
        t_p = self.heap[pos_parent]
        while self.__cmp(t, t_p) and pos > 0:
            self.heap[pos],self.heap[pos_parent] = self.heap[pos_parent],self.heap[pos]
            pos = pos_parent
            pos_parent = self.parent(pos)
            t_p = self.heap[pos_parent]
            

    def __trickle_down(self) -> None:
        """Swap the first item in the heap with one of its children
        until the heap property holds.
        """
        pos = 0
        count = len(self.heap)
        if pos < count:
            done = False
            while not done:
                t = self.heap[pos] 
                pos_l = self.left_child(pos)
                pos_r = self.right_child(pos)
                if pos_r < count:
                    t_l = self.heap[pos_l]
                    t_r = self.heap[pos_r]
                    if self.__cmp(t_l, t) or self.__cmp(t_r, t):
                        dest = pos_l if self.__cmp(t_l, t_r) else pos_r
                        self.heap[pos],self.heap[dest] = self.heap[dest],self.heap[pos]
                        pos = dest
                    else:
                        done = True
                elif pos_l < count:
                    t_l = self.heap[pos_l]
                    if self.__cmp(t_l, t):
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

class MinHeap(Heap):
    """A min heap."""
    def __init__(self) -> None:
        super().__init__(Heap.Direction.ASC)

class MaxHeap(Heap):
    """A max heap."""
    def __init__(self) -> None:
        super().__init__(Heap.Direction.DESC)
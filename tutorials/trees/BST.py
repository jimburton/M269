import random
from Tree import *

class BST(Tree):
    """A Binary Search Tree."""

    def insert(self, item) -> 'BST':
        """Insert a new item to the BST."""
        if item < self.value:
            if self.left is None:
                return BST(self.value, BST(item, None, None), self.right)
            else:
                return BST(self.value, self.left.insert(item), self.right)
        elif item > self.value:
            if self.right is None:
                return BST(self.value, self.left, BST(item, None, None))
            else:
                return BST(self.value, self.left, self.right.insert(item))
        else:
            return self

    def remove(self, item) -> 'BST':
        """Remove an item from the BST."""
        if item == self.value:
            if not self.left is None:
                return BST(self.left.value, BST.merge(self.left.left, self.left.right), self.right)
            elif not self.right is None:
                return BST(self.right.value, self.left, BST.merge(self.right.left, self.right.right))
            else:
                return None
        elif item < self.value:
            if not self.left is None:
                return BST(self.value, self.left.remove(item), self.right)
            else:
                return self
        elif item > self.value:
            if not self.right is None:
                return BST(self.value, self.left, self.right.remove(item))
            else:
                return self


    def search(self, item) -> bool:
        """Search BST for an item."""
        if item == self.value:
            return True
        elif item < self.value and not self.left is None:
            return self.left.search(item)
        elif item > self.value and not self.right is None:
            return self.right.search(item)
        else:
            return False
        
    @classmethod    
    def build(cls, ns: set) -> 'BST':
        """Build a BST from a set."""
        t = Tree(ns.pop(), None, None)
        for n in ns:
            t.insert(n)
        return t
    
    @classmethod
    def merge(cls, t1: 'BST', t2: 'BST') -> 'BST':
        """Merge two BSTs."""
        lst = t2.traverse()
        random.shuffle(lst)
        for n in lst:
            t1.insert(n)
        return t1
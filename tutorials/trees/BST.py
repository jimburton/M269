import random
from Tree import *

class BST(Tree):
    """A Binary Search Tree."""

    def insert(self, item) -> 'BST':
        """Insert a new item to the BST."""
        pass

    def remove(self, item) -> 'BST':
        """Remove an item from the BST."""
        pass

    def search(self, item) -> bool:
        """Search BST for an item."""
        pass
        
    @classmethod    
    def build(cls, ns: set) -> 'BST':
        """Build a BST from a set."""
        pass
    
    @classmethod
    def merge(cls, t1: 'BST', t2: 'BST') -> 'BST':
        """Merge two BSTs."""
        pass
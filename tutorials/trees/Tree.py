class Tree:
    """A binary tree."""

    def __init__(self, value, left: 'Tree', right: 'Tree'):
        """ Construct a new Tree."""
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None   
    
    def leaves(self) -> list:
        """Return the leaves of this Tree as a list."""
        (lh,rh) = self.maybe_children(Tree.leaves, [])
        val = [self.value] if self.is_leaf() else []
        return [*lh, *val, *rh]

    def children(self) -> list:
        """Return the immediate children of this Tree in a list."""
        result = [self.left] if self.left else []
        if self.right:
            result.append(self.right)
        return result

    
    def to_list(self) -> list:
        """An in-order traversal."""
        (lh,rh) = self.maybe_children(Tree.to_list, [])
        return [*lh, self.value, *rh]
        
    def height(self) -> int:
        """Return the height of the Tree."""
        (lh,rh) = self.maybe_children(Tree.height, 0)
        # the use of maybe_children is equivalent to:
        # lh = self.left.height() if self.left else 0
        # rh = self.right.height() if self.right else 0
        return 1 + max(lh, rh)
    
    def count_nodes(self) -> int:
        """Count the nodes in the Tree."""
        (ln,rn) = self.maybe_children(Tree.count_nodes, 0)
        return 1 + ln + rn 
    
    def maybe_children(self, fn, default) -> tuple:
        """Apply fn to left and right children if present,
           substituting the default value if they aren't.
           Removes the need for repeatedly checking if
           left and right are None.
        """
        lh = fn(self.left) if self.left else default
        rh = fn(self.right) if self.right else default
        return (lh,rh)

    def copy(self) -> 'Tree':
        """Make a deep copy of the Tree."""
        (lh,rh) = self.maybe_children(Tree.copy, None)
        return Tree(self.value, lh, rh)
    
    def __lt__(self, other: 'Tree') -> bool:
        """Return True if the label of this Tree is less than the label of other."""
        return self.value < other.value 
    
    def __str__(self):
        """Format this Tree for printing."""
        (lh,rh) = self.maybe_children(Tree.__str__, "None")
        return f"Tree val: {self.value} [{lh}] [{rh}]"
    
    #def __eq__(self, other: 'Tree') -> bool:
    #    """Compare two Trees."""
    #    if other is None:
    #        return False
    #    return self.to_list().sort() == other.to_list().sort()
    

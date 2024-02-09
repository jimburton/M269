class Tree:
    """A binary tree."""

    def __init__(self, value, left: 'Tree', right: 'Tree'):
        """ Construct a new Tree."""
        self.value = value
        self.left = left
        self.right = right

    def height(self) -> int:
        """Return the height of the Tree."""
        pass
    
    def count_nodes(self) -> int:
        """Count the nodes in the Tree."""
        pass
    
    def traverse(self) -> list:
        """An in-order traversal."""
        pass

    def copy(self) -> 'Tree':
        """Make a deep copy of the Tree."""
        pass
    
    def maybe_children(self, fn, default) -> tuple:
        """Apply fn to left and right children if present,
           substituting the default value if they aren't.
           Removes the need for repeatedly checking if
           left and right are None.
        """
        pass
    
    def __eq__(self, other: 'Tree') -> bool:
        """Compare two Trees."""
        pass
    
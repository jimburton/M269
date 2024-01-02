from Set import Set

class LinkedSet(Set):
    """A linked list implementation of the set ADT."""

    class Node:
        """A node in a linked list."""
        def __init__(self, item: object):
            """Initialise the node with the given item."""
            self.item = item
            self.next = None

    def __init__(self):
        """Initialise the list to be empty."""
        self.head = None

    def size(self) -> int:
        """Return the cardinality of this set."""
        pass

    def member(self, item: object) -> bool:
        """Returns True if item is a member of this set."""
        pass

    def add(self, item: object) -> None:
        """Add item to the set. No duplicates allowed."""
        pass

    def tolist(self) -> [object]:
        """Convert the set to a list of its members."""
        pass

    def clone(self) -> Set:
        """Create a shallow copy of this set."""
        pass

    def isdisjoint(self, other: Set) -> bool:
        """Returns True if the other set is disjoint from this one."""
        pass

    def issubset(self, other: Set) -> bool:
        """Returns True if this set is a subset of the other one."""
        pass

    def issuperset(self, other: Set) -> bool:
        """Returns True if this set is a superset of the other one."""
        pass
        
    def union(self, other: Set) -> Set:
        """Returns a new set which is the union of this set and other."""
        pass

    def intersection(self, other: Set) -> Set:
        """Returns a new set which is the intersection of this set and other."""
        pass

    def difference(self, other: Set) -> Set:
        """Returns a new set which is the difference of this set and other."""
        pass

    def remove(self, item: object) -> None:
        """Remove the item.
        Raises KeyError if item is not a member of the set.
        """
        pass

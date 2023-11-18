from Set import Set

class LinkedSet(Set):
    """A linked list implementation of the set ADT."""

    class Node:
        """A node in a linked list.
        """
        def __init__(self, item: object):
            """Initialise the node with the given item."""
            self.item = item
            self.next = None

    def __init__(self):
        """Initialise the list to be empty."""
        self.head = None

    def size(self) -> int:
        pass

    def member(self, item: object) -> bool:
        pass

    def add(self, item: object) -> None:
        pass

    def isdisjoint(self, other: Set) -> bool:
        pass

    def issubset(self, other: Set) -> bool:
        pass

    def tolist(self) -> [object]:
        pass

    def issuperset(self, other: Set) -> bool:
        pass
        
    def clone(self) -> Set:
        pass

    def union(self, other: Set) -> Set:
        pass

    def intersection(self, other: Set) -> Set:
        pass

    def difference(self, other: Set) -> Set:
        pass

    def remove(self, item: object) -> None:
        pass

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
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.next
        return count

    def member(self, item: object) -> bool:
        current = self.head
        while current != None:
            if current.item == item:
                return True
            current = current.next
        return False

    def add(self, item: object) -> None:
        if self.member(item):
            pass
        n = LinkedSet.Node(item)
        n.next = self.head
        self.head = n

    def isdisjoint(self, other: Set) -> bool:
        current = self.head
        while current != None:
            if other.member(current.item):
                return False
            current = current.next
        return True

    def issubset(self, other: Set) -> bool:
        current = self.head
        while current != None:
            if not other.member(current.item):
                return False
            current = current.next
        return True

    def tolist(self) -> [object]:
        result = []
        current = self.head
        while current != None:
            result.append(current.item)
            current = current.next
        return result

    def issuperset(self, other: Set) -> bool:
        # why can't we refer to other.head?
        for i in other.tolist():
            if not self.member(i):
                return False
        return True
        
    def clone(self) -> Set:
        result = LinkedSet()
        current = self.head
        while current != None:
            result.add(current.item)
            current = current.next
        return result

    def union(self, other: Set) -> Set:
        result = self.clone()
        for i in other.tolist():
            result.add(i)
        return result

    def intersection(self, other: Set) -> Set:
        result = LinkedSet()
        current = self.head
        while current != None:
            if other.member(current.item):
                result.add(current.item)
            current = current.next
        return result

    def difference(self, other: Set) -> Set:
        result = LinkedSet()
        current = self.head
        while current != None:
            if not other.member(current.item):
                result.add(current.item)
            current = current.next
        return result

    def remove(self, item: object) -> None:
        current  = self.head
        if current == None:
            raise KeyError("item not found")
        if current.item == item:
            self.head = current.next
        else:
            previous = current
            current = current.next
            found = False
            while current != None:
                if current.item == item:
                    previous.next = current.next
                    found = True
                    break
                else:
                    previous = current
                    current = current.next
            if not found:
                raise KeyError("item not found")

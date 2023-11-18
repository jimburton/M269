# M269 Tutorial: Practice Block One

These exercises build on the code and exercises in the M269 Book in
Chapter 6. Familiarity with the ADTs in that chapter and their
implementations in Python is assumed.

## The Set ADT

A *set* is an unordered collection of items with no duplicates. As such,
it is a good choice of data structure if we know that we don't want
any duplicate data. In mathematical notation, sets are shown as a
comma-separated list within braces, e.g. `{1, 2, 3}`.  

Python provides sets as part of its standard library but we are going
to implement our own. Our set ADT supports the following operations:

* We can *add* and *remove* items from a set. When adding items,
duplicates are silently ignored.
* We can query the *size* of a set (also called its *cardinality*).
* We can find out whether a particular object is a *member* of a given
set.
* We can take the *union* of two sets, *A* and *B*, resulting in a
third set, *C*. *C* contains all elements of *A* and *B* (and nothing
else). For instance, the union of the sets `{1, 2, 3, 4}` and `{3, 4,
5}` is `{1, 2, 3, 4, 5}`.
* We can take the *intersection* of two sets, *A* and *B*, resulting in a third
set, *C*. *C* contains exactly those elements which are in both *A*
and *B*. The intersection of the sets `{1, 2, 3, 4}` and `{3, 4,
5}` is `{3, 4}`.
* We can take the *difference* of a set, *A*, with respect to a second
set, *B*, resulting in a third set, *C*. The difference of the set
`{1, 2, 3, 4}` with respect to the set `{3, 4, 5}` is `{1, 2}`. The
difference of `{3, 4, 5}` with respect to `{1, 2, 3, 4}` and  is
`{5}`.
* We can calculate whether two sets are *disjoint*, which is true if they
  have no elements in common.
* We can calculate whether one set, *A*, is a *subset* of another, *B*. This
  is true if and only if all elements of *A* are elements of *B*. *B*
  might also contain other elements, but it contains at least the
  elements of *A*. 
* We can calculate whether one set, *A*, is a *superset* of another, *B*. This
  is true if and only if all elements of *B* are elements of *A*.
* We can calculate whether two sets are *equal*. This is true if they have
  exactly the same members (remember that order is unimportant).
* We can convert a set to a ordinary Python list.

This ADT is expressed in the file [src/Set.py](src/Set.py).

## Implementing the Set ADT

We will implement the Set ADT using a *linked list*, in the style of
Section 6.7 from the book. The first item in a linked list is called
`head`. If `head` is null the list is empty. Each element of one of our
linked lists is instance of the `Node` class. A node contains an
`item`, which is the data, and a pointer to the next node in the list,
called `next`.  To traverse the list we can start with `head` and
keep following the `next` pointers until they lead to `None`,
indicating that this is the end of the list.

Open the file (`src/LinkedSet.py`) to carry out the
implementation. Several of the methods we need to implement are
identical, or almost identical, to methods in the `LinkedList` class
from Section 6.7 of the book. For instance, finding the size of a
`LinkedSet` is done in exactly the same way as finding the length of a
`LinkedList`, so rereading that section will help if you need
pointers. Also, you can see my versionof the finished code in the
`solutions` branch of this repository. 

The `size` method, in common with many of the others, requires us to
*traverse* the collection. This is done by taking a reference to the
`head` then calling the `next` pointer repeatedly until we reach the
end. This is the pattern:

```python
current = head
while current != None:
	# do something
	current = current.next
```

1. Implement the `size` method. You can do this by initialising a
   counter then using the pattern above to increment it for every item
   in the set. Finally, return the counter.
2. Use the same pattern to implement the `member` method. If you
   encounter a node whose item is equal to the thing we're looking
   for, return `True`. If you get all the way to the end of the set
   without doing that, the element was not in the list so return
   `False`.
3. Implement the `add` method. Remember, no duplicates are
   allowed. Use the `member` method to check for that. If the new item
   is not a duplicate, make a new `Node` object with `next` pointing
   to the current `head`, then reassign `head` to the new object.
4. Implement the `isdisjoint` method. This should return `True` if the
   two sets (`self` and `other`) have no elements in common. Loop
   through the current set and return `False` as soon as you
   encounter an item which is in the other set.
5. Implement the `issubset` method. This is very similar to the
   `isdisjoint` method except that you want to return `False` as soon
   as you encounter an element which is not in the other set.
6. Implement the `tolist` method. No hints for this one, it should be
   easy :-)
7. Implement the `issuperset` method. Similar to the previous problem
   but in this case we want to loop through the *other* set. Note that
   you **cannot** refer to `other.head` -- why? To work around this
   convert the other set to a list and loop through that.
8. Implement the `clone` method. Make a new set then loop through the
   current set adding items to the new one.
9. Implement the `clone` method, which creates a "shallow" copy of the
   current set. (A shallow copy of a collection, *A*, is one in which a
   new collection, *B*, is created then references to every element of
   *A* is inserted to *B*. A deep copy is one which *copies* of the
   elements of *A* are inserted to *B*.)
10. Implement the `union` method, where the result should contain all
    elements of both sets. One way to do this is to clone the current
    set then loop through the other set inserting elements into the
    clone.
11. Implement the `intersection` method, where the result should
    contain just those elements that are in both sets.
12. Implement the `difference` method, where the result should contain
    those elements of the current set which are not members of the
    other set.
13. Implement the `remove` method. This one is tricky, and I advise
    you to think of two cases: the simple case where the item to
    remove is equal to the item in `head`, and the more complex case
    where the item to remove is somewhere further on within the
    set. In the latter case you will remove the item by changing the
    `next` pointer of the node before the target item to point to the
    node after the target item. So, you will need to maintain two
    pointers in your loop: one to the current item and one to the
    previous.
14. Implement the `__eq__` method for equality between sets. This is a
    builtin method that means we can now use the `==` operator on
    sets. Two sets are equal if they contain exactly the same
    elements, regardless of order.
	
## Testing

Tests are provided in the file [src/TestLinkedSet.py](src/TestLinkedSet.py). You should
run these often to check your progress. The tests are *unit tests*, a
standard testing framework which isn't covered in this module. If you
are using an IDE such as VS Code, PyCharm or IntelliJ, there will be
built in support for running these tests from the IDE. If you aren't
sure how to do this we can discuss it in the tutorial.

You can however run the tests from the command line. If you navigate
to the `src` directory in a terminal the following command runs all
tests:

```
$ python3 -m unittest -v TestLinkedSet.Testing
```

You can also run a specific test by giving its name. For instance, to
run the test `test_add_and_size`:

```
$ python3 -m unittest -v TestLinkedSet.Testing.test_add_and_size
```


## Discussion

1. What is the time complexity of `member`?
2. What is the time complexity of `intersection`?
3. The fact that our implementation uses a linked list means it is not
   very efficient. Could we use a more efficient data structure to
   implement the Set ADT? Bear in mind that we can't guarantee that
   the objects in our set can be ordered. If we could find a more
   efficient underlying data structure, what would happen to the
   complexity of `intersection`?

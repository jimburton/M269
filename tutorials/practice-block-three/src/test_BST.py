import unittest
from random import (shuffle)
from BST import *

class Testing(unittest.TestCase):

    def setUp(self):
        self.bst0 = BST(0, None, None)

    def test_insert_and_search(self):
        """ Test that the insert and search methods work."""
        lst = list(range(99))
        random.shuffle(lst)
        bst = BST(0, None, None)
        for n in lst:
            bst = bst.insert(n)
        for n in range(99):
            self.assertTrue(bst.search(n))

    def test_remove(self):
        """ Test that the remove method works."""
        bst1 = BST(0, None, None)
        print(bst1)
        self.assertTrue(bst1.remove(0) is None)
        print(bst1)
        self.assertTrue(bst1.remove(1) == bst1)

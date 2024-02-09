import unittest
from Tree import *

class Testing(unittest.TestCase):

    def setUp(self):
        self.tree0 = Tree(0, None, None)
        self.tree1 = Tree(1, self.tree0.copy(), self.tree0.copy())

    def test_count_nodes(self):
        """ Test that the count_nodes method works."""
        self.assertEqual(self.tree0.copy().count_nodes(), 1)
        self.assertEqual(self.tree1.copy().count_nodes(), 3)

    def test_height(self):
        """ Test that the height method works."""
        self.assertEqual(self.tree0.copy().height(), 1)
        self.assertEqual(self.tree1.copy().height(), 2)

    def test_traverse(self):
        """ Test that the traverse method works."""
        self.assertEqual(self.tree0.copy().traverse(), [0])
        self.assertEqual(self.tree1.copy().traverse(), [0,1,0])

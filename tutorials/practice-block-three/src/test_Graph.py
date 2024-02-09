import unittest
from Graph import *

class Testing(unittest.TestCase):

    def setUp(self):
        self.tree0 = Graph.build({'A', 'B', 'C', 'D'}, {('A', 'B'), ('A', 'C')})
        self.tree1 = Graph.build({'A', 'B', 'C', 'D', 'E', 'F', 'G'}
                                 , {('A', 'B'), ('A', 'C'), ('A', 'E')
                                , ('B', 'D'), ('B', 'F'), ('C', 'G')
                                , ('E', 'F')})
        self.tree_discon = Graph.build({'A', 'B', 'C', 'D', 'E', 'F', 'G'}     # nodes
                                       , {('A', 'C'), ('A', 'F')})

    def test_disconnected(self):
        """ Test that the disconnected method returns the right set of nodes."""
        self.assertEqual(self.tree0.disconnected(), {'D'})
        self.assertEqual(self.tree1.disconnected(), set())
        self.assertEqual(self.tree_discon.disconnected(), {'B', 'D', 'G', 'E'})

    def test_elem(self):
        """ Test that the elem method works."""
        self.assertTrue(self.tree0.elem('A'))
        self.assertFalse(self.tree0.elem('E'))
        self.assertFalse(Graph().elem('X'))

    def test_neighbours_out_finds_neighbours(self):
        """ Test that the neighbours_out method works."""
        n1 = self.tree0.neighbours_out('A')
        self.assertEqual(set(n1), {'B', 'C'})
        n2 = self.tree0.neighbours_out('B')
        self.assertEqual(set(n2), set())
        n3 = self.tree1.neighbours_out('B')
        self.assertEqual(set(n3), {'D', 'F'})

    def test_neighbours_out_fails_when_missing(self):
        """ Test that the neighbours_out method throws a LookupError if
            the node is not present.#
        """
        with self.assertRaises(LookupError) as context:
            self.tree0.neighbours_out('X')

    def test_neighbours_in_finds_neighbours(self):
        """ Test that the neighbours_in method works."""
        n1 = self.tree0.neighbours_in('A')
        self.assertEqual(set(n1), set())
        n2 = self.tree0.neighbours_in('B')
        self.assertEqual(set(n2), {'A'})
        n3 = self.tree1.neighbours_in('F')
        self.assertEqual(set(n3), {'B', 'E'})

    def test_neighbours_in_fails_when_missing(self):
        """ Test that the neighbours_in method throws a LookupError if
            the node is not present.
        """
        with self.assertRaises(LookupError) as context:
            self.tree0.neighbours_in('X')
    
    def test_traverse_df_rec_visit_all(self):
        """ Test that the recursive depth-first traversal visits all nodes. """
        df_rec = self.tree1.traverse_df_rec('A')
        # check that all nodes are visited
        self.assertEqual(len(self.tree1.nodes), len(df_rec))

    def test_traverse_df_rec_visit_first(self):
        """ Test that the recursive depth-first traversal visits the first node
            first.
        """
        df_rec = self.tree1.traverse_df_rec('A')
        # check that the first node is correct
        self.assertEqual(df_rec[0], 'A')

    def test_traverse_df_rec_fails_when_missing(self):
        """ Test that the recursive depth-first traversal throws a LookupError if
            the node is not present.
        """
        with self.assertRaises(LookupError) as context:
            self.tree0.traverse_df_rec('X')

    def test_traverse_df_rec_reaches_deadend(self):
        """ Test that whichever direction the recursive depth-first traversal
            goes, it continues as far as it can.
        """
        df_rec = self.tree1.traverse_df_rec('A')
        m = 'A'
        for n in df_rec[1:]:
            # for every node in the traversal, it is either
            # . the child of the previous node, or
            # . a deadend
            self.assertTrue(n in self.tree1.neighbours_out(m)
                            or len(self.tree1.neighbours_out(n)) == 0)
            if len(self.tree1.neighbours_out(n)) == 0:
                m = 'A'
            else:
                m = n

    def test_traverse_df_iter_visit_all(self):
        """ Test that the iterative depth-first traversal visits all nodes. """
        df_iter = self.tree1.traverse_df_iter('A')
        # check that all nodes are visited
        self.assertEqual(len(self.tree1.nodes), len(df_iter))

    def test_traverse_df_rec_visit_first(self):
        """ Test that the iterative depth-first traversal visits the first node
            first.
        """
        df_iter = self.tree1.traverse_df_iter('A')
        # check that the first node is correct
        self.assertEqual(df_iter[0], 'A')

    def test_traverse_df_iter_fails_when_missing(self):
        """ Test that the iterative depth-first traversal throws a LookupError if
            the node is not present.
        """
        with self.assertRaises(LookupError) as context:
            self.tree0.traverse_df_iter('X')

    def test_traverse_df_iter_reaches_deadend(self):
        """ Test that whichever direction the iterative depth-first traversal
            goes, it continues as far as it can.
        """
        df_iter = self.tree1.traverse_df_iter('A')
        m = 'A'
        for n in df_iter[1:]:
            # for every node in the traversal, it is either
            # . the child of the previous node, or
            # . a deadend
            self.assertTrue(n in self.tree1.neighbours_out(m)
                            or len(self.tree1.neighbours_out(n)) == 0)
            if len(self.tree1.neighbours_out(n)) == 0:
                m = 'A'
            else:
                m = n

    def test_traverse_bf_visit_all(self):
        """ Test that the breadth-first traversal visits all nodes. """
        bf = self.tree1.traverse_bf('A')
        self.assertEqual(len(bf), len(self.tree1.nodes))

    def test_traverse_bf_visit_first(self):
        """ Test that the breadth-first traversal visits the first node
            first.
        """
        bf = self.tree1.traverse_bf('A')
        # check that the first node is correct
        self.assertEqual(bf[0], 'A')

    def test_traverse_bf_visit_children(self):
        """ Test that the breadth-first traversal visits the children
            of the first node.
        """
        bf = self.tree1.traverse_bf('A')
        # check that the children of A are visited first
        self.assertEqual(set(bf[1:4]), {'B', 'C', 'E'})

    def test_traverse_bf_visit_grandchildren(self):
        """ Test that the breadth-first traversal visits the grandchildren
            of the first node.
        """
        bf = self.tree1.traverse_bf('A')
        # check that the grandchildren of A are visited next
        self.assertEqual(set(bf[4:]), {'D', 'F', 'G'})

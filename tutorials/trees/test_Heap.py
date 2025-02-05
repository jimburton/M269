import unittest
import random
from Heap import *

class Testing(unittest.TestCase):

    def setUp(self):
        self.small_list = [12,3,99,25,3,7,32,4]

    def test_insert(self):
        """Test that inserting preserves the heap property."""
        heap = MinHeap()
        for n in self.small_list:
            heap.insert(Tree(('x',n), None, None))
        for i,t in enumerate(heap.heap):
            l = heap.left_child(i)
            r = heap.right_child(i)
            if l < len(heap.heap):
                self.assertLessEqual(heap.get_frequency(t), heap.get_frequency(heap.heap[l]))
            if r < len(heap.heap):
                self.assertLessEqual(heap.get_frequency(t), heap.get_frequency(heap.heap[r]))

    def test_remove(self):
        """Test that removing preserves the heap property."""
        heap = MinHeap()
        nums = self.small_list.copy()
        for n in nums:
            heap.insert(Tree(('x',n), None, None))
        freqs = []
        while(heap.size() > 0):
            t = heap.remove()
            freqs.append(heap.get_frequency(t))
        nums.sort()
        self.assertEqual(nums, freqs)

    def test_randoms(self):
        """Test that inserting and removing a lot of random values 
        preserves the heap property."""
        heap = MinHeap()
        for i in range(0,20):
            n = random.randint(1,1000)
            heap.insert(Tree(('x',n), None, None))
        freq = heap.get_frequency(heap.remove())
        while(heap.size() > 0):
            new_freq = heap.get_frequency(heap.remove())
            self.assertLessEqual(freq, new_freq)
            freq = new_freq
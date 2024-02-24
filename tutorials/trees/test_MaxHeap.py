import unittest
import random
from Heap import *
from HuffmanTree import *

class Testing(unittest.TestCase):

    def setUp(self):
        self.small_list = [12,3,99,25,3,7,32,4]

    def test_insert(self):
        """Test that inserting preserves the heap property."""
        heap = MaxHeap()
        for n in self.small_list:
            heap.insert(HuffmanTree(('x',n), None, None))
        for i,t in enumerate(heap.heap):
            l = heap.left_child(i)
            r = heap.right_child(i)
            if l < len(heap.heap):
                self.assertGreaterEqual(t.get_frequency(), heap.heap[l].get_frequency())
            if r < len(heap.heap):
                self.assertGreaterEqual(t.get_frequency(), heap.heap[r].get_frequency())

    def test_remove(self):
        """Test that removing preserves the heap property."""
        heap = MaxHeap()
        nums = self.small_list.copy()
        for n in nums:
            heap.insert(HuffmanTree(('x',n), None, None))
        freqs = []
        while(heap.size() > 0):
            t = heap.remove()
            freqs.append(t.get_frequency())
        nums.sort(reverse=True)
        self.assertEqual(nums, freqs)

    def test_randoms(self):
        """Test that inserting and removing a lot of random values 
        preserves the heap property."""
        heap = MaxHeap()
        for i in range(0,20):
            n = random.randint(1,1000)
            heap.insert(HuffmanTree(('x',n), None, None))
        freq = heap.remove().get_frequency()
        while(heap.size() > 0):
            new_freq = heap.remove().get_frequency()
            self.assertGreaterEqual(freq, new_freq)
            freq = new_freq
import unittest
from Huffman import *

class Testing(unittest.TestCase):

    def setUp(self):
        self.msg0 = "Hi, how are you?"

    def test_freq_table(self):
        """ Test we can build the frequency table correctly."""
        ft = freq_table(self.msg0)
        self.assertEqual(len(ft.keys()), len(set(self.msg0))) # one key per unique char
        for c in self.msg0:
            self.assertTrue(c in ft.keys()) # each char in freq table
            self.assertEqual(ft[c], self.msg0.count(c)) # freq counts are correct

    def test_empty_freq_table(self):
        """ Test we can make a frequency table for the empty string."""
        ft = freq_table("")
        self.assertEqual(len(ft.keys()), 0)

    def test_htree_from_freqtable(self):
        """ Test we can make a Huffman tree from a frequency table."""
        ht = htree_from_freqtable(freq_table(self.msg0))
        self.assertEqual(ht.value[1], len(self.msg0)) # counts all chars
        self.assertEqual(set(map(lambda x: x[0], ht.leaves())), set(self.msg0)) # leaves match unique chars

    def test_build_code(self):
        """Test we can build the Huffman code."""
        code = build_code(htree_from_freqtable(freq_table(self.msg0)))
        self.assertEqual(len(code.keys()), len(set(self.msg0))) # one code entry per unique char
        for c in self.msg0:
            self.assertTrue(c in code.keys()) # each char in code

    def test_tree_from_code(self):
        """Test we can build the Huffman tree."""
        ht = htree_from_freqtable(freq_table(self.msg0))
        (c,d) = encode(self.msg0)
        t = tree_from_code(c)
        # reconstructed tree matches original
        self.assertEqual(ht.count_nodes(), t.count_nodes())
        self.assertEqual(set(map(lambda x: x[0], ht.leaves())), set(map(lambda x: x[0], t.leaves())))
        
    def test_huffman_codec(self):
        """ Test we can code and decode."""
        ft = freq_table(self.msg0)
        ht = htree_from_freqtable(ft)
        code = build_code(ht)
        (c,d) = encode(self.msg0)
        t = tree_from_code(c)
        secret = decode(c, d)
        self.assertEqual(secret, self.msg0)
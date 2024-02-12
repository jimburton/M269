from queue import PriorityQueue
from Tree import *

def freq_table(input: str) -> dict:
    """Build a frequency table from the input string."""
    pass

def htree_from_freqtable(ft: dict) -> Tree:
    """Build a Huffman tree from a frequency table."""
    pass

def build_code(t: Tree) -> dict:
    """Build a Huffman code from a Huffman tree."""
    pass

def encode(input: str) -> tuple:
    """Make the Huffman coding of the input string to a tuple of Huffman code 
       and encoded data.
    """
    pass

def tree_from_code(code: dict) -> Tree:
    """Reconstruct the Huffman tree from a Huffman code."""
    pass

def decode(code: dict, data: list) -> str:
    """Decode the data using the Huffman code."""
    pass

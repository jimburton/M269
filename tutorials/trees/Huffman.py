from queue import PriorityQueue
from Tree import *

def freq_table(input: str) -> dict:
    """Build a frequency table from the input string."""
    ft = dict()
    for c in input:
        ft[c] = ft[c] + 1 if c in ft else 1
    return ft

def htree_from_freqtable(ft: dict) -> Tree:
    """Build a Huffman tree from a frequency table."""
    queue = PriorityQueue()
    # Put a leaf node into the queue for every key,value in the frequency table.
    for (k,v) in ft.items():
        queue.put((v, Tree((k,v), None, None)))
    # Combine and enqueue the first two nodes in the queue until there is only one left. 
    while queue.qsize() > 1:
        (f1,n1) = queue.get()
        (f2,n2) = queue.get()
        queue.put((f1+f2, Tree(('',f1+f2), n1, n2)))
    return queue.get()[1]

def build_code(t: Tree) -> dict:
    """Build the Huffman code from a Huffman tree."""
    def make_path(t: Tree, path: list) -> dict:
        if t.is_leaf():
            return {t.value[0]: path}
        else:
            lh = make_path(t.left, path + [False]) if t.left else {} # Recurse left.
            rh = make_path(t.right, path + [True]) if t.right else {} # Recurse right.
            lh.update(rh) # Combine the dicts.
            return lh 
    return make_path(t, [])

def encode(input: str) -> tuple:
    """Make the Huffman coding of the input string. The coding is a tuple of the Huffman code
       and the encoded data.
    """
    ft = freq_table(input)
    ht = htree_from_freqtable(ft)
    code = build_code(ht)
    data = []
    for c in input:
        data.extend(code[c])
    return (code, data)

def tree_from_code(code: dict) -> Tree:
    """Reconstruct the Huffman tree from a Huffman code."""
    t = Tree(None, None, None)
    node = t
    for (k,path) in code.items():
        for i in range(len(path)):
            leaf = i == len(path)-1 # Last step in the path.
            next = Tree((k,0), None, None) if leaf else Tree(None, None, None)
            # Add a right or left node to the Tree and move in that direction.
            if path[i]:
                if node.right is None:
                    node.right = next
                node = node.right
            else:
                if node.left is None:
                    node.left = next
                node = node.left
        node = t
    return t

def decode(code: dict, data: list) -> str:
    """Decode a list of bools using a Huffman code."""
    t = tree_from_code(code)
    node = t # Start at the root.
    secret = ""
    for b in data:
        if node.is_leaf():
            node = t # Return to the root.
        node = node.right if b else node.left # Follow the path.
        if node.is_leaf():
            secret += node.value[0] # Add a char to the decoded message.
    return secret

#def print(t: Tree):
#    pt = PrettyPrintTree(lambda x: x.children(), lambda x: x.value)
#    pt(t)

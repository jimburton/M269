from queue import PriorityQueue
from Tree import *

def freq_table(input: str) -> dict:
    ft = dict()
    for c in input:
        if c in ft:
            ft[c] += 1
        else:
            ft[c] = 1
    return ft

def htree_from_freqtable(ft: dict) -> Tree:
    queue = PriorityQueue()
    for (k,v) in ft.items():
        queue.put((v, Tree((k,v), None, None)))
    while queue.qsize() > 1:
        (f1,n1) = queue.get()
        (f2,n2) = queue.get()
        queue.put((f1+f2, Tree(('',f1+f2), n1, n2)))
    return queue.get()[1]

def build_code(t: Tree) -> dict:
    def make_path(t: Tree, path: list) -> dict:
        if t.left is None and t.right is None:
            return {t.value[0]: path}
        else:
            lh = make_path(t.left, path + [False]) if t.left else {}
            rh = make_path(t.right, path + [True]) if t.right else {}
            lh.update(rh)
            return lh 
    return make_path(t, [])

def encode(input: str) -> tuple:
    ft = freq_table(input)
    ht = htree_from_freqtable(ft)
    code = build_code(ht)
    data = []
    for c in input:
        data.extend(code[c])
    return (code, data)

def tree_from_code(code: dict) -> Tree:
    t = Tree(None, None, None)
    node = t
    for (k,path) in code.items():
        for i in range(len(path)):
            leaf = i == len(path)-1
            next = Tree((k,0), None, None) if leaf else Tree(None, None, None)
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
    t = tree_from_code(code)
    node = t
    secret = ""
    for b in data:
        if node.is_leaf():
            node = t
        node = node.right if b else node.left
        if node.is_leaf():
            secret += node.value[0]
    return secret

#def print(t: Tree):
#    pt = PrettyPrintTree(lambda x: x.children(), lambda x: x.value)
#    pt(t)

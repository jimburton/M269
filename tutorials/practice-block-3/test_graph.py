from solution import *

tree0 = Graph.build({'A', 'B', 'C', 'D'}, {('A', 'B'), ('A', 'C')})

tree1 = Graph.build({'A', 'B', 'C', 'D', 'E', 'F', 'G'}
                    , {('A', 'B'), ('A', 'C'), ('A', 'E')
                       , ('B', 'D'), ('B', 'F'), ('C', 'G')
                       , ('E', 'F')})

def test_disconnected():
    assert tree0.disconnected() == {'D'}
    assert tree1.disconnected() == set()
    
def test_traverse_df():
    print(tree1.traverse_df('A'))
    assert tree1.traverse_df('A') == ['A', 'E', 'F', 'B', 'D', 'C', 'G']

def test_traverse_bf():
    print(tree1.traverse_bf('A'))
    assert tree1.traverse_bf('A') == ['A', 'E', 'B', 'C', 'F', 'D', 'G']

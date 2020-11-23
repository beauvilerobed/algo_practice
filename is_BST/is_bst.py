import sys
from collections import defaultdict


class TreeNode:
    def __init__(self, value, children):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, num_of_nodes):
        self.num_of_nodes = num_of_nodes
        self.nodes = {}
    
    def add(self, u, v):
        self.nodes[u].append(v)

    def is_bst(self)


class Tree:
    def __init__(self, data, children=None):
        self.data = data
        self.children = []
        if children != None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.data

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
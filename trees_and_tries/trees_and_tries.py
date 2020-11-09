
class Tree:
    """
    A tree can be defined as a node with its children
    """
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


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.in_end = False
        self.children = {}

    def __repr__(self):
        return self.char


# class Trie:
#     def __init__(self):
#         self.root = TrieNode("")

#     def insert(self, word):

#     def dfs(self, node, prefix):

#     def search(self, x):
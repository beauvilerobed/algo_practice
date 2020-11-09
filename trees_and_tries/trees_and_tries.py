import sys


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


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.in_end = False
        self.visited = False
        self.children = {}

    def __repr__(self):
        return self.char


class Trie:
    def __init__(self):
        self.root = TrieNode("")
        self.word_number = 0
        self.bag = []

    def insert(self, word):
        self.word_number += 1

        node = self.root
        # will help determeine duplicates
        count = 0
        for char in word:
            # if char is one of the nodes continue down the trie
            if char in node.children:
                count += 1
                node = node.children[char]
            # else create a new node and attach to trie
            else:
                count -= 1
                new = TrieNode(char)
                node.children[char] = new
                node = new

        if count == len(word):
            self.word_number -= 1

        node.in_end = True

    def search(self, word):
        node = self.root
        index = 0
        while True:
            # find the index for which the prefix is already in the trie
            if index == len(word):
                return "word found"
            elif word[index] in node.children:
                node = node.children[word[index]]
                index += 1
            else:
                return "word not found"

    def dfs(self, node, prefix):
        if node.in_end:
            self.bag.append(prefix)
                
        for child in node.children:
            child_node = node.children[child]
            prefix = prefix + child_node.char
            self.dfs(child_node, prefix)
            prefix = prefix[:-1]

    def query(self, prefix):
        self.bag = []
        node = self.root

        count = 0
        for char in prefix:
            if char in node.children:
                node = node.children[char]
                count += 1
            elif count == 0:
                return self.bag
            else:
                break
        
        self.dfs(node, prefix)

        return self.bag


def main():
    data_set = sys.stdin.readlines()
    trie = Trie()
    for data in data_set:
        data = data.rstrip()
        trie.insert(data)
    
    print(trie.word_number)
    print(trie.query(''))
    print(trie.search(input("What word would you like to search: ")))
    print(trie.query(input("What prefix would you like to search: ")))
    trie.insert("my")
    trie.insert("hello")
    print(trie.query(''))
    print(trie.word_number)


if __name__ == '__main__':
    main()
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

    def insert(self, word):
        self.word_number += 1

        node = self.root
        index = 0
        
        # find the index for which the prefix is already in the trie
        while True:
            if word[index] in node.children:
                node = node.children[word[index]]
                index += 1
            else:
                break
        
        # words in the trie could be a substring of inserted word
        if index == len(word) and node.in_end == True:
            node.in_end = False

        # add the remaining suffix to the node found
        for char in word[index:]:
            new = TrieNode(char)
            node.children[char] = new
            node = new
            
        node.in_end = True

    def search(self, word):
        node = self.root
        index = 0
        while True:
            # find the index for which the prefix is already in the trie
            if index >= len(word):
                break
            elif word[index] in node.children:
                node = node.children[word[index]]
                index += 1
            else:
                break
        # word is in trie only when all char in the some trie path
        if index == len(word):
            return "word found"
        else:
            return "no word found"

    def dfs(self, node, bag, word):
        if node.in_end:
            bag.append(word)
            word = ''
            
        for child in node.children:

            child_node = node.children[child]
            
            if not child_node.visited:
                child_node.visited = True
                word += child_node.char
            self.dfs(child_node, bag, word)
            word = word[:-1]

    def all_words(self):
        bag = []
        node = self.root
        self.dfs(node, bag, '')

        return bag


def main():
    data_set = sys.stdin.readlines()
    trie = Trie()
    for data in data_set:
        data = data.rstrip()
        trie.insert(data)
    
    print(trie.all_words())
    print(trie.word_number)
    print(trie.search(input("What word would you like to search: ")))


if __name__ == '__main__':
    main()
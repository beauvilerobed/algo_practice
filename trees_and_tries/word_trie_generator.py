import os
import random
from trees_and_tries import Trie


def generate_words():
    path = os.getcwd() + '/words.txt'
    with open(path, 'r') as f:
        data = f.readlines()
        words = [word.rstrip() for word in data]

    return words

def generate_trie(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    return trie

def generate_other_words(words):
    other_words = []
    for i in range(100):
        if i % 3 == 0:
            index = random.randint(0, 999)
            other_words.append('0'+ words[index])
        else:
            index = random.randint(0, 999)
            other_words.append(words[index])

    return other_words
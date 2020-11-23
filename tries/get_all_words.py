# task: find all words stored in Trie

import sys
from tries import Trie


def get_all_words(trie):
    words = trie.query('')
    return words


def main():
    data_set = sys.stdin.readlines()
    trie = Trie()
    for data in data_set:
        data = data.rstrip()
        trie.insert(data)

    print(get_all_words(trie))


if __name__ == '__main__':
    main()


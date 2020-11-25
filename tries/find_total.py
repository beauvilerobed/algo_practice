# python3

# task: find the total number of words stored in Trie

import sys
from tries import Trie


def get_total_naive(trie):
    words = trie.query('')
    return len(words)


def get_total(trie):
    return trie.word_number


def main():
    data_set = sys.stdin.readlines()
    trie = Trie()
    for data in data_set:
        data = data.rstrip()
        trie.insert(data)

    print(get_total(trie))
    print(get_total_naive(trie))


if __name__ == '__main__':
    main()

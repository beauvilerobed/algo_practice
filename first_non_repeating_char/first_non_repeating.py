#python3

# task: Find the first non-repeated character in a String

import sys
from collections import Counter


def find_non_repeating(string):
    hash_it = Counter(string)
    for i in range(len(string)):
        char = string[i]
        if hash_it[char] == 1:
            return i + 1
    
    return -1


def main():
    data = sys.stdin.readline()
    data = data.rstrip()
    print(find_non_repeating(data))


if __name__ == '__main__':
    main()

# python3

import sys
from collections import Counter

def check_if_anagram_naive(string1, string2):
    string1 = sorted([char for char in string1])
    string2 = sorted([char for char in string2])

    if string1 == string2:
        return 0
    else:
        return -1

def check_if_anagram(string1, string2):
    hash_it1 = Counter(string1)
    hash_it2 = Counter(string2)

    for val in hash_it1:
        if val not in hash_it2:
            return -1
        elif hash_it1[val] != hash_it2[val]:
            return -1

    return 0

def main():
    strings = sys.stdin.readlines()
    string1 = strings[0].rstrip()
    string2 = strings[1].rstrip()

    print(check_if_anagram(string1,string2))


if __name__ == '__main__':
    main()

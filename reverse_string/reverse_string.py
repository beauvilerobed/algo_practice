# python3

# Task: reverse a string iteratively and recursively

import sys


def reverse_iterative(string):
    n = len(string)
    string = [char for char in string]
    for i in range(n // 2):
        string[i], string[n - 1 - i] = string[n - 1 - i], string[i]

    string = "".join(string)
    return string


def reverse_recursive_util(string, left, right):
    if left < right:
        string[left], string[right] = string[right], string[left]
        reverse_recursive_util(string, left + 1, right - 1)


def reverse_recursive(string):
    string = [char for char in string]
    reverse_recursive_util(string, 0, len(string)-1)
    return "".join(string)


def main():
    data = sys.stdin.readline()
    data = data.rstrip()
    print(reverse_iterative(data))
    print(reverse_recursive(data))


if __name__ == '__main__':
    main()

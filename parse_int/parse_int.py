# python3

import sys


def parse_int(string):
    n = len(string)
    if n == 0:
        return None

    base_ten = 1
    integer = 0

    for i in range(n):
        key = ord(string[n - i - 1]) - 48
        num = key * base_ten
        integer += num
        base_ten *= 10

    return integer


def main():
    string = input()
    print(parse_int(string) + 1)


if __name__ == '__main__':
    main()

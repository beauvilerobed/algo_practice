# python3

import sys


def square_root(n):
    if n == 0:
        return 0

    # Newton–Raphson method solve y ** 2 - x = 0
    x = 1
    y = .5 * x + n / (2 * x)
    diff = float("inf")

    while diff > 0:
        x = y
        y = .5 * x + n / (2 * x)
        diff = abs(x - y)

    return x


def main():
    n = float(input())
    print(square_root(n))


if __name__ == '__main__':
    main()

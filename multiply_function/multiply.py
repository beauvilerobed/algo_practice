# pyhton3

# task: Write a multiply function that multiples 2
# integers without using the * symbol

import sys


def multiply(a, b):
    c = 1
    d = 1

    if a < 0:
        c = -1
    if b < 0:
        d = -1

    num = multiply_positive(abs(a), abs(b))
    return c * d * num


def multiply_positive(a, b):
    result = 0

    for _ in range(a):
        result += b

    return result


def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    a = nums[0]
    b = nums[1]
    print(multiply(a, b))


if __name__ == '__main__':
    main()

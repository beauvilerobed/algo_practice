import sys


def parse_int(string):
    n = len(string)
    array_of_10 = [10 ** (n - i - 1) for i in range(n)]
    nums = {str(i+1) : i + 1 for i in range(9)}

    integer = 0

    for i in range(n):
        key = string[i]
        num = nums[key] * array_of_10[i]
        integer += num

    return integer


def main():
    string = input()
    print(parse_int(string) + 1)


if __name__ == '__main__':
    main()
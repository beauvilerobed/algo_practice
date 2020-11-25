# python3

# task: find second max value in array

import sys


def find_second_max_naive(nums):
    nums = set(nums)
    if len(nums) <= 1:
        return None

    nums = list(nums)
    nums.sort()

    return nums[-2]


def find_second_max(nums):

    first_max = -float("inf")
    index = 0
    for i, val in enumerate(nums):
        if val > first_max:
            first_max = val
            index = i

    second_max = -float("inf")
    for j, val in enumerate(nums):
        if val != first_max and index != j and val > second_max:
            second_max = val

    # case where array only has repeated numbers or is empty
    if second_max == -float("inf"):
        return None

    return second_max


def main():
    input_vals = sys.stdin.readline()
    nums = list(map(int, input_vals.split()))
    print(find_second_max(nums))


if __name__ == '__main__':
    main()

# python3

import sys


def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        index = return_min_index(nums[i:], i)
        nums[i], nums[index] = nums[index], nums[i]

    return nums


def return_min_index(nums, i):
    index = 0
    min_val = float("inf")

    for j, val in enumerate(nums):
        if val < min_val:
            index = j + i
            min_val = val

    return index


def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    print(selection_sort(nums))


if __name__ == '__main__':
    main()

# pyhton3

# Task: Find the second smallest value in a binary search tree

import sys
from bst import BST
import numpy as np
from find_smallest import find_smallest 


def find_second_smallest(bst):
    first_min = find_smallest(bst)
    string_nums = str(bst)
    char_nums = string_nums.split()
    nums = list(map(int, char_nums))
    nums = remove_occur(nums, first_min)

    return nums[0]


def remove_occur(nums, value):
    new_arr = []
    for num in nums: 
        if num == value:
            pass
        else:
            new_arr.append(num)

    return new_arr


def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    bst = BST()
    for num in nums:
        bst.insert(num)
    print(find_second_smallest(bst))


if __name__ == '__main__':
    main()

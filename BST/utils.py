# python3

from numpy import random
from bst import BST


def find_second_min(nums):
    nums = set(nums)
    if len(nums) <= 1:
        return None
    nums = list(nums)
    nums.sort()

    return nums[1]


def generate_bsts_and_nums_small():
    nums = [[0], [-1, 1, 2], [1, 1, 1]]
    bsts = make_bsts(nums)

    return bsts, nums


def generate_bsts_and_nums(num=1000):
    rand_nums = random.randint(-num, num, size=(num//10, num))
    bsts = make_bsts(rand_nums)
    rand_nums = sort_nums(rand_nums)

    return bsts, rand_nums


def make_bsts(nums):
    bsts = []
    for vals in nums:
        bst = BST()
        for num in vals:
            bst.insert(num)
        bsts.append(bst)

    return bsts


def sort_nums(nums):
    for vals in nums:
        vals.sort()
    return nums


def generate_expected_actual(bsts, nums):
    expected = []
    actual = []
    for vals, bst in zip(nums, bsts):
        for num in vals:
            if num % 3 == 0:
                bst.delete(num)

        num_string = str(bst)
        char_nums = num_string.split()
        bst_nums = list(map(int, char_nums))
        sorted_bst_nums = sorted(bst_nums)

        expected.append(sorted_bst_nums)
        actual.append(bst_nums)
    
    return expected, actual

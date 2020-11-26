import random
import numpy
from numpy import random


def generate_sorted_nums(number=1000):
    nums = random.randint(-number, number, size=(number, number))
    for nums_with in nums:
        nums_with.sort()
    return nums


def generate_rotations(nums):
    for i in range(len(nums)):
        vals = nums[i]
        n = len(vals)
        pivot = random.randint(n-1)
        first = vals[:pivot]
        second = vals[pivot:]
        nums[i] = numpy.concatenate([second, first])

    return nums

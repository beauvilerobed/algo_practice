import random

def generate_sorted_nums(number=1000):
    nums =[[random.randint(-number, number) for _ in range(random.randint(number // 2, number))] for _ in range(random.randint(number // 2, number))]
    for nums_with in nums:
        nums_with.sort()
    return nums

def generate_rotations(nums):
    for i in range(len(nums)):
        num = nums[i]
        n = len(num)
        pivot = random.randint(0,n-1)
        first = num[:pivot]
        second = num[pivot:]
        nums[i] = second + first
    
    return nums
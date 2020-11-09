#python3

# merge two sorted arrays

import sys
import collections

def remove_even_naive(nums):
    
    index = 0
    while index < len(nums):
        if nums[index] % 2 == 0:
            nums.pop(index)
        else:
            index += 1

    return nums

def remove_even(nums):
    # create a counter for number of occurances
    counter = collections.Counter(nums)
    result = []
    
    # set the even keys to zero
    for val in counter:
        if val % 2 == 0:
            counter[val] = 0

    # add the remaining keys to result
    for val in nums:
        if val in counter and counter[val] > 0:
            result.append(val)
            counter[val] -= 1

    return result

def remove_even_less(nums):
    new_nums = [x for x in nums if x % 2 != 0]
    return new_nums

def remove_even_in_place(nums):
    n = len(nums)
    right = len(nums) - 1 
    left = 0

    while left < right:
        if (nums[left] % 2 == 0) & (nums[right] % 2 == 1):
            nums[left], nums[right] = nums[right], nums[left]
        if nums[right] % 2 == 0:
            right -= 1
        if nums[left] % 2 == 1:
            left += 1

    for i in range(n):
        if nums[n - 1 - i] % 2 == 0:
            nums.pop()

    return nums


def main():
    nums = sys.stdin.readlines()
    nums = list(map(int, nums))
    print(remove_even(nums))


if __name__ == '__main__':
    main()
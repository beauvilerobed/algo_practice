# python3

# task: Write a program that, given an array A[] of 
# n numbers and another number x, determines whether 
# or not there exist two elements in S whose sum is 
# exactly x.

import sys
from collections import Counter


def two_sum(nums, target):
    nums = Counter(nums)
    for num in nums:
        val = target - num
        if val in nums:
            if val == num and nums[val] > 1:
                return num, num
            
            elif val != num:
                return num, val

    return None

def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    print(two_sum(nums, 10))


if __name__ == '__main__':
    main()
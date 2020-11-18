#python3

# Given a list, find the most frequent element in it. 
# If there are multiple elements that appear maximum 
# number of times, print any one of them.

import sys
from collections import Counter


def find_most_frequent(nums):
    if len(nums) < 1:
        return None

    nums = Counter(nums)

    most_frequent = -float("inf")
    value = 0

    for num in nums:
        if nums[num] > most_frequent:
            value = num
            most_frequent = nums[num]
    
    return value


def main():
    data = sys.stdin.readline()
    data = data.rstrip()
    nums = list(map(int, data.split()))
    print(find_most_frequent(nums))


if __name__ == '__main__':
    main()
    
# python3

# find the k smallest number in a unsorted array

import sys
from heapq import heapify, heappop


def k_smallest_naive(nums, k):
    nums = set(nums)
    nums = list(nums)
    if len(nums) < k:
        return None

    nums.sort()
    return nums[k - 1]


def k_smallest(nums, k):
    nums = set(nums)
    nums = list(nums)
    heapify(nums)

    if len(nums) < k:
        return None

    min = float("inf")
    for _ in range(k):
        min = heappop(nums)

    return min


def main():
    k = int(sys.stdin.readline())
    data = sys.stdin.readline()
    data = list(map(int, data.split()))
    print(k_smallest(data, k))


if __name__ == '__main__':
    main()

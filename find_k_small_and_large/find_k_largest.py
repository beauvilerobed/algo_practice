# python3

# find the k largest number in a unsorted array


from heapq import heappop, heapify
import sys


def k_largest_naive(nums, k):
    nums = set(nums)
    nums = list(nums)
    if len(nums) < k:
        return None

    nums.sort(reverse=True)
    return nums[k - 1]


def k_largest(nums, k):
    nums = set(nums)
    nums = list(nums)
    nums = [-num for num in nums]
    heapify(nums)

    if k > len(nums):
        return None

    k_max = 0
    for _ in range(k):
        k_max = heappop(nums)

    return -k_max


def main():
    k = int(sys.stdin.readline())
    data = sys.stdin.readline()
    values = list(map(int, data.rstrip().split()))
    print(k_largest(values, k))


if __name__ == '__main__':
    main()

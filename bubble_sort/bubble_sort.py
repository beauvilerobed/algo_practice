# python3

import sys


def bubble_sort(nums):
    n = len(nums)

    for _ in range(n):
        for j in range(n-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums


def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    print(bubble_sort(nums))


if __name__ == '__main__':
    main()
# python3

import sys
import random


def quick_sort(nums):

    def quick_sort_util(left, right):
        if left > right:
            return
            
        p = pick_pivot(left, right)
        nums[left], nums[p] = nums[p], nums[left]

        start, end = partition_around(nums, left, right)
        quick_sort_util(left, start-1)
        quick_sort_util(end + 1, right)
    
    n = len(nums)
    quick_sort_util(0, n-1)
    
    return nums

def pick_pivot(left, right):
    return random.randint(left, right)

def partition_around(nums, left, right):
    pivot = nums[left]
    start = left + 1
    next_index = left + 1

    while next_index <= right:
        if nums[next_index] < pivot:
            nums[next_index], nums[start] = nums[start], nums[next_index] 
            next_index += 1
            start += 1

        elif nums[next_index] >= pivot:
            next_index += 1
    
            
    start = start - 1
    nums[start], nums[left] = nums[left], nums[start]
    end = start

    return start, end
                


def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    print(quick_sort(nums))


if __name__ == '__main__':
    main()
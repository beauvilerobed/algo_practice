# python3

import sys


def insertion_sort(nums):
    n = len(nums)
    for i in range(n):

        front = nums[:i+1]
        tail = nums[i+1:]
        index = find_insertion_point(front)

        num_to_insert = front.pop()
        front.insert(index, num_to_insert)
        nums = front + tail
        
    return nums

def find_insertion_point(nums):
    last_num = nums[-1]
    n = len(nums)

    if nums[0] > last_num:
        return 0
    
    for j in range(1, n):
        if last_num <= nums[j] and last_num >= nums[j-1]:
            return j
    
    return n - 1

def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    print(insertion_sort(nums))


if __name__ == '__main__':
    main()
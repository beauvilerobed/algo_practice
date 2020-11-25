# python3

# task: Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})

import sys


def binary_on_rotation(nums, target):

    index = find_min_max(nums)

    if index is None:
        return index

    if nums[index] <= target and target <= nums[-1]:
        new_nums = nums[index:]
        return binary_search(new_nums, target)

    elif nums[0] <= target:
        new_nums = nums[:index]
        return binary_search(new_nums, target)


def find_min_max(nums):
    n = len(nums)
    if n == 0:
        return None

    index = 0
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            index = i+1
            break

    return index


def binary_search(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    mid = (left + right) // 2

    while left <= right:
        if target == nums[mid]:
            return target

        elif target < nums[mid]:
            right = mid - 1

        elif target > nums[mid]:
            left = mid + 1

        mid = (left + right) // 2

    return None


def main():
    target = int(sys.stdin.readline())
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    print(binary_on_rotation(nums, target))


if __name__ == '__main__':
    main()

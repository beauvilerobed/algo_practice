# python3

import sys


def merge_sort(nums):
    n = len(nums)

    if n < 2:
        return nums

    first_half = nums[:n // 2]
    second_half = nums[n // 2:]
    first_sorted_half = merge_sort(first_half)
    second_sorted_half = merge_sort(second_half)
    sorted_nums = merge_nums(first_sorted_half, second_sorted_half)

    return sorted_nums


def merge_nums(nums1, nums2):
    nums = []
    n = len(nums1)
    m = len(nums2)
    index1 = 0
    index2 = 0
    while index1 < n and index2 < m:
        if nums1[index1] <= nums2[index2]:
            nums.append(nums1[index1])
            index1 += 1

        else:
            nums.append(nums2[index2])
            index2 += 1

    if index1 != n:
        temp = nums1[index1:]
        nums += temp

    if index2 != m:
        temp = nums2[index2:]
        nums += temp

    return nums


def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    print(merge_sort(nums))


if __name__ == '__main__':
    main()

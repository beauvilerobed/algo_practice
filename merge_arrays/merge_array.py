# python 3

# merge two sorted arrays

import sys


def merge_array_naive(nums1, nums2):
    result = nums1 + nums2
    result.sort()
    return result


def merge_array(nums1, nums2):
    # initialize two pointers for each array
    n = len(nums1)
    m = len(nums2)
    index1 = 0
    index2 = 0
    result = []

    # loop throught each array at the same time to
    # to see which value to add to the result
    while index1 < n and index2 < m:
        if nums1[index1] > nums2[index2]:
            value = nums2[index2]
            result.append(value)
            index2 += 1

        elif nums1[index1] < nums2[index2]:
            value = nums1[index1]
            result.append(value)
            index1 += 1

        else:
            value1 = nums1[index1]
            value2 = nums2[index2]
            result.append(value1)
            result.append(value2)
            index1 += 1
            index2 += 1

    # one of the pointers must have reached n or m
    # add the array that didnt reach n to result
    if index1 != n:
        result = result + nums1[index1:]

    if index2 != m:
        result = result + nums2[index2:]

    return result


def main():
    input_vals = sys.stdin.readlines()
    nums1 = list(map(int, input_vals[0].split()))
    nums2 = list(map(int, input_vals[1].split()))
    print(merge_array(nums1, nums2))


if __name__ == '__main__':
    main()

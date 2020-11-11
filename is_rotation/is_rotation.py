# python3

# task: Given 2 integer arrays, determine if the 2nd 
# array is a rotated version of the 1st array. 
# Ex. Original Array A={1,2,3,5,6,7,8} 
# Rotated Array B={5,6,7,8,1,2,3}

import sys


def is_rotation(array1, array2):
    n = len(array1)
    m = len(array2)

    if m != n:
        return -1

    index1 = 0
    index2 = 0

    # first find where the first element is located in the second array.
    while index2 < m:
        if array1[index1] == array2[index2]:
            break
        index2 += 1

        if index2 == m:
            return -1

    # loop through both array to see if elements are not matching, they should.
    while index2 < m:
        if array1[index1] != array2[index2]:
            return -1
        index1 += 1
        index2 += 1

    # initialize second index and begin loop again
    # first index should be in appropriate location
    index2 = 0
    # loop through both array to see if element are not matching
    while index1 < n:
        if array1[index1] != array2[index2]:
            return -1
        index1 += 1
        index2 += 1

    return 0


def main():
    data = sys.stdin.readlines()
    array1 = list(map(int, data[0].rstrip().split()))
    array2 = list(map(int, data[1].rstrip().split()))
    print(is_rotation(array1, array2))


if __name__ == '__main__':
    main()
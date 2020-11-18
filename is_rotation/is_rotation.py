# python3

# task: Given 2 integer arrays, determine if the 2nd 
# array is a rotated version of the 1st array. 
# Ex. Original Array A={1,2,3,5,6,7,8} 
# Rotated Array B={5,6,7,8,1,2,3}

import sys


def is_rotation(array1, array2):
    m = len(array1)
    n = len(array2)
    if m != n:
        return -1
    elif m == 0:
        return 0

    index2 = find_first_elem_in_second_arr(array1, array2)
    index1 = loop_thru_both(array1, array2, index2)
    result = loop_thru_both(array2, array1, index1)

    return -1 if result == -1 else 0


def find_first_elem_in_second_arr(arr1, arr2):
    m = len(arr2)
    index2 = 0

    while index2 < m:
        if arr1[0] == arr2[index2]:
            return index2
        index2 += 1

    return -1


def loop_thru_both(arr1, arr2, index):
    if index == -1:
        return -1

    index1 = 0
    m = len(arr2)

    while index < m:
        if arr1[index1] != arr2[index]:
            return -1
        index1 += 1
        index += 1
    
    return index1


def main():
    data = sys.stdin.readlines()
    array1 = list(map(int, data[0].rstrip().split()))
    array2 = list(map(int, data[1].rstrip().split()))
    print(is_rotation(array1, array2))


if __name__ == '__main__':
    main()

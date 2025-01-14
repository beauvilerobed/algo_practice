# python3

# Your task is to compute the total number of comparisons used to sort the given input
# file by QuickSort. As you know, the number of comparisons depends on which elements 
# are chosen as pivots, so we'll ask you to explore three different pivoting rules.

# WARNING: The Partition subroutine can be implemented in several different ways, 
# and different implementations can give you differing numbers of comparisons.

# Compute the number of comparisons, using the 
# "median-of-three" pivot rule. [The primary motivation behind this rule is to 
# do a little bit of extra work to get much better performance on input arrays 
# that are nearly sorted or reverse sorted.] 
# 
# In more detail, you should choose 
# the pivot as follows. Consider the first, middle, and final elements of the 
# given array. (If the array has odd length it should be clear what the "middle" 
# element is; for an array with even length 2k, use the kth element as the 
# "middle" element. So for the array 4 5 6 7, the "middle" element is the 
# second one ---- 5 and not 6!) Identify which of these three elements is 
# the median (i.e., the one whose value is in between the other two), and 
# use this as your pivot.

# EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), 
# middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, 
# you would use 4 as your pivot element.

import sys
import statistics
import copy


global global_count
global_count = 0


def count_sort(input_array, choose_pivot):

    def partition_around_array(input_array, left, right):
        global global_count
        global_count += max(right - left, 0)
        if right - left < 1:
            return

        pivot_index = int()
        if choose_pivot == 'right':
            pivot_index = select_last(left, right)
        elif choose_pivot == 'middle':
            pivot_index = select_middle(input_array, left, right)
        elif choose_pivot == 'left':
            pivot_index = select_first(left, right)
        input_array[left], input_array[pivot_index] =\
        input_array[pivot_index], input_array[left]

        i = left + 1
        for j in range(left + 1, right + 1):
            if input_array[j] < input_array[left]:
                input_array[i], input_array[j] = input_array[j], input_array[i]
                i += 1

        input_array[left], input_array[i-1] =\
        input_array[i-1], input_array[left]

        if i != left + 1:
            partition_around_array(input_array, left, i-2)
        partition_around_array(input_array, i, right)

    partition_around_array(input_array, 0, len(input_array) - 1)

    global global_count
    count = global_count
    global_count = 0
    return count


def select_first(left, right):
    return left


def select_last(left, right):
    return right


def select_middle(input_array, left, right):
    middle = left + ((right - left) // 2)
    nums = [input_array[left], input_array[right], input_array[middle]]
    median = statistics.median(nums)
    for index in left, right, middle:
        if input_array[index] == median:
            return index
        

def main():
    data = sys.stdin.read()
    data_set1 = list(map(int, data.split()))
    data_set2 = copy.copy(data_set1)
    data_set3 = copy.copy(data_set1)
    print(count_sort(data_set1, 'left'))
    print(count_sort(data_set2, 'right'))
    print(count_sort(data_set3, 'middle'))


if __name__ == '__main__':
    main()

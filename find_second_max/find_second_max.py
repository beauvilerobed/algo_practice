# python3

# find second max value in array

import sys

def find_second_max_naive(nums):
    nums = set(nums)
    # check if all elements or the same of input is empty array
    if len(nums) <= 1:
        return None

    nums = list(nums)
    # else sort the array
    nums.sort()   

    #return second to last index
    return nums[-2]


def find_second_max(nums):

    first_max = -float("inf")
    index = 0
    # find first max first
    for i, val in enumerate(nums):
        if val > first_max:
            first_max = val
            index = i

    second_max = -float("inf")
    # then with first max chosen find second max
    for j, val in enumerate(nums):
        if val != first_max and index != j and val > second_max:
            second_max = val

    # case where array only has repeated numbers or is empty
    if second_max == -float("inf"):
        return None

    return second_max


def main():
    input_vals = sys.stdin.readline()
    nums = list(map(int, input_vals.split()))
    print(find_second_max(nums))


if __name__ == '__main__':
    main()
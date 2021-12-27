# python3

# The goal of this problem is to implement a variant of the 2-SUM algorithm.

# Your task is to compute the number of target values t in the interval
# [-10000,10000] (inclusive) such that there are distinct numbers x,y in the
# input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line
# addition to the algorithm from lecture.)


import sys


def two_sums(nums, target):
    hash_it = set(nums)
    count = 0
    for num in nums:
        temp = target - num
        if temp != num and temp in hash_it:
            count += 1
            break

    return count


def find_two_sum_total(case, targets):
    count = 0
    for target in targets:
        count += two_sums(case, target)

    return count


def main():
    data = sys.stdin.read()
    data_set = list(map(int, data.split()))
    values = [-2, 3, 8, 11]
    is_sum = two_sums(data_set, values)
    print(is_sum)


if __name__ == '__main__':
    main()

# python3

# Parenthesize an arithmetic expression to maxi- mize its value.

# Input. A string s = s_0s_1s_2...s_2n of length at most 29. Each symbol 
# at an even position of s is a digit (that is, an integer from 
# 0 to 9) while each symbol at an odd position is one of three 
# operations from {+,-,×}.

# Output. The maximum value of the given arithmetic expression 
# among all possible orders of applying arithmetic operations.

import operator


def find_maximum_value(data_set):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    operator_signs = []
    nums = []
    for val in data_set:
        if val in ops:
            operator_signs.append(ops[val])
        else:
            nums.append(int(val))

    min_matrix = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    max_matrix = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

    # base case
    for i in range(len(nums)):
        min_matrix[i][i] = nums[i]
        max_matrix[i][i] = nums[i]

    for s in range(1, len(nums)):
        for i in range(len(nums) - s):
            j = i + s
            min_matrix[i][j], max_matrix[i][j] = min_max(min_matrix,
                                                         max_matrix,
                                                         operator_signs,
                                                         i,
                                                         j)

    return max_matrix[0][len(nums) - 1]


def min_max(min_matrix, max_matrix, operator_signs, i, j):
    minimum = float("inf")
    maximum = -float("inf")

    # run through all subexpresions split by k for find the min and max
    for k in range(i, j):
        a = operator_signs[k](min_matrix[i][k], min_matrix[k + 1][j])
        b = operator_signs[k](min_matrix[i][k], max_matrix[k + 1][j])
        c = operator_signs[k](max_matrix[i][k], min_matrix[k + 1][j])
        d = operator_signs[k](max_matrix[i][k], max_matrix[k + 1][j])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return minimum, maximum


def main():
    print(find_maximum_value(input()))


if __name__ == "__main__":
    main()

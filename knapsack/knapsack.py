# python3

# 1
# In this programming problem and the next you'll code up the knapsack algorithm.

# Let's start with a warm-up.

# You can assume that all numbers are positive. You should assume that item weights 
# and the knapsack capacity are integers.

# The output should be the value of the optimal solution.

# 2
# This problem also asks you to solve a knapsack instance, but a much bigger one.

# This instance is so big that the straightforward iterative implemetation uses an 
# infeasible amount of time and space. So you will have to be creative to compute 
# an optimal solution. One idea is to go back to a recursive implementation, 
# solving subproblems -- and, of course, caching the results to avoid redundant work 
# -- only on an "as needed" basis. Also, be sure to think about appropriate data 
# structures for storing and looking up solutions to subproblems.

# The output should be the value of the optimal solution.

import sys
import copy


def knapsack(values, number_items, knapsack_size):
    a = [[0 for _ in range(knapsack_size + 1)] for _ in range(number_items)]

    for i in range(number_items):
        for x in range(knapsack_size + 1):
            value = values[i][0]
            weight = values[i][1]
            if weight > x:
                a[i][x] = a[i-1][x]
            else:
                a[i][x] = max(a[i-1][x], a[i-1][x - weight] + value)

    return a[number_items-1][knapsack_size]


def knapsack_fast(values, number_items, knapsack_size):
    a = [0 for _ in range(knapsack_size + 1)]
    b = [0 for _ in range(knapsack_size + 1)]
    for i in range(number_items):
        weight = values[i][1]
        b[:weight] = a[:weight]

        for x in range(weight, knapsack_size + 1):
            value = values[i][0]
            not_added = a[x]
            added = a[x - weight] + value
            if added > not_added:
                b[x] = added
        a = copy.copy(b)

    return a[-1]


def main():
    data = sys.stdin.read()
    data_set = data.split()
    values = []
    info = list(map(int, data_set[0].split()))
    number_items = info[1]
    knapsack_size = info[0]
    for values in data_set[1:]:
        int_values = list(map(int, values.split()))
        values.append(int_values)

    print("knapsack:", knapsack(values, number_items, knapsack_size))
    print("knapsack fast:", knapsack_fast(values, number_items, knapsack_size))


if __name__ == '__main__':
    main()

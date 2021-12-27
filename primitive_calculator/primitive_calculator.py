# python3

# Find the minimum number of operations needed to get a positive 
# integer n from 1 using only three operations: add 1, multiply 
# by 2, and multiply by 3.

# Input. An integer 1 ≤ n ≤ 106.

# Output. In the first line, output the minimum number k of 
# operations needed to get n from 1. In the second line, output 
# a sequence of intermediate numbers. That is, the second line 
# should contain positive integers a0, a1, ... , ak such that 
# a0 = 1, ak = n, and for all 1 ≤ i ≤ k, ai is equal to either 
# ai−1 + 1, 2ai−1, or 3ai−1. If there are many such sequences, 
# output any one of them.

def compute_operations(n):
    result = [0, [0, [1]]]

    for k in range(2, n + 1):
        # find the min previously compute operation value
        # of k/2 k/3 (if they exist) and k - 1 dynamically
        values = result[k - 1]
        if k % 2 == 0:
            if result[k // 2][0] < values[0]:
                values = result[k // 2]

        if k % 3 == 0:
            if result[k // 3][0] < values[0]:
                values = result[k // 3]

        # then add to result of appropriate value
        next_value = values[0] + 1
        next_array = values[1] + [k]
        result.append([next_value, next_array])

    return result[-1][1]


def main():
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)


if __name__ == '__main__':
    main()

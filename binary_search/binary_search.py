# pyhton3

# Input: A sorted array K=[k0, ... ,kn-1] of 
# 1 ≤ n ≤ 3 × 104 distinct integers and an array 
# Q = [q0 , ... , qm-1] of 1 ≤ m ≤ 105 integers.

# Output: For all i from 0 to m-1, output an index 
# 0 ≤ j ≤ n-1 such that kj = qi or -1, if there is no such index.

def binary_search_naive(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    start = 0
    end = len(keys) - 1

    mid = ((end - start) // 2) + start
    while start <= end:
        if keys[mid] == query:
            return mid
        elif keys[mid] > query:
            end = mid - 1
        elif keys[mid] < query:
            start = mid + 1

        mid = ((end - start) // 2) + start

    return -1


def main():
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')


if __name__ == '__main__':
    main()

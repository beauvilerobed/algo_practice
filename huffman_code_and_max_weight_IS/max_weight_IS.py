# python3

# In this programming problem you'll code up the dynamic programming algorithm for 
# computing a maximum-weight independent set of a path graph.

# Your task in this problem is to run the dynamic programming algorithm 
# (and the reconstruction procedure) on this data set. The question is: of the 
# vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones belong to the maximum-weight 
# independent set? By "vertex 1" we mean the first vertex of the graph -- there is 
# no vertex 0--.

# The output is a 8-bit string, where the ith bit should be 1 if the ith of these 
# 8 vertices is in the maximum-weight independent set, and 0 otherwise. For example, 
# if you think that the vertices 1, 4, 17, and 517 are in the maximum-weight 
# independent set and the other four vertices are not, then you should enter the 
# string 10011010 in the box below.

# NOTE: If the graph doesn't have a node, then it doesn't belong to the maximum-weight 
# independent set, and therefore its bit would be 0. For example, if the size of the 
# graph is 500, then the two last bits correspondning to nodes 517 and 997 would be 0.

import sys


def max_weight_IS(weights, length):
    possible_vertices = {0: 0, 1: 1, 2: 2, 3: 3, 16: 4, 116: 5, 516: 6, 996: 7}
    result = ['0' for _ in range(8)]

    max_weights = [0, weights[0]]

    for i in range(2, length):
        choice = int()
        if max_weights[i-1] > max_weights[i-2] + weights[i-1]:
            choice = max_weights[i-1]
        else:
            choice = max_weights[i-2] + weights[i-1]
        max_weights.append(choice)

    reconstructed_weights = []
    i = len(max_weights)

    while i >= 0:
        if max_weights[i-1] >= max_weights[i-2] + weights[i - 1]:
            i = i - 1
        else:
            reconstructed_weights.append(i - 1)
            i = i - 2

    for val in reconstructed_weights:
        if val in possible_vertices:
            result[possible_vertices[val]] = '1'

    return "".join(result)


def main():
    data = sys.stdin.read()
    data_set = list(map(int, data.split()))
    length = data_set[0]
    print(max_weight_IS(data_set[1:], length))


if __name__ == '__main__':
    main()

# python3

# Your task is to compute the "shortest shortest path". Precisely, you must first 
# identify which, if any, of the three graphs have no negative cycles. For each 
# such graph, you should compute all-pairs shortest paths and remember the smallest 
# one (i.e., compute \min_{u,v \in V} d(u,v)min u,v∈V​d(u,v), where d(u,v)d(u,v) 
# denotes the shortest-path distance from uu to vv).

# If each of the three graphs has a negative-cost cycle, then enter "NULL" 
# in the box below. If exactly one graph has no negative-cost cycles, then 
# enter the length of its shortest shortest path in the box below. If two or 
# more of the graphs have no negative-cost cycles, then enter the smallest of 
# the lengths of their shortest shortest paths in the box below.

from file_reader import read_file
import numpy as np
import os
import glob


def floyd_warshal(graph, n):
    A = np.full((n, n), float('inf'))
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i, j] = 0
            if (i, j) in graph:
                A[i, j] = graph[i, j]
            if i != j and (i, j) not in graph:
                A[i, j] = float('inf')
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i, j] = min(A[i, j], A[i, k] + A[k, j])

    for i in range(n):
        if A[i,i] < 0:
            return 'Null'

    np.fill_diagonal(A, np.inf)
    return A.min()


def main():
    file_path = os.getcwd() + '/files/*'
    paths = glob.glob(file_path)

    graphs = []
    for path in paths:
        graph_data = read_file(path)
        graphs.append(graph_data)

    for graph_data in graphs:
        graph = graph_data[0]
        n = graph_data[1]
        print(floyd_warshal(graph, n))


if __name__ == '__main__':
    main()

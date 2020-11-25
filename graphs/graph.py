# python3

import sys
from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V  # number of nodes
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)

    def dfs_util(self, node, visited):
        visited[node] = True
        self.data.append(node)
        if node in self.edges:
            for child in self.edges[node]:
                if visited[child] is False:
                    self.dfs_util(child, visited)

    def dfs(self):
        self.data = []
        visited = [False] * (self.V + 1)

        for node in self.edges:
            if visited[node] is False:
                self.dfs_util(node, visited)

        return self.data

    def bfs_util(self, node, visited):
        queue = [node]

        while len(queue) > 0:
            node = queue.pop(0)
            self.bag.append(node)
            visited[node] = True
            if node in self.edges:
                for edge in self.edges[node]:
                    if visited[edge] is False:
                        queue.append(edge)

    def bfs(self):
        self.bag = []
        visited = [False] * (self.V + 1)
        for node in self.edges:
            if visited[node] is False:
                self.bfs_util(node, visited)

        return self.bag


def main():
    data_set = sys.stdin.readlines()
    size = int(data_set[0].rstrip())
    graph = Graph(size)
    for data in data_set[1:]:
        data = list(map(int, data.split()))
        u = data[0]
        v = data[1]
        graph.add_edge(u, v)

    print(graph.dfs())
    print(graph.bfs())


if __name__ == '__main__':
    main()

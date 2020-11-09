#python3

import sys
from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.visited = False
    
    def __repr__(self):
        return str(self.data)

class Graph:
    def __init__(self):
        self.nodes = defaultdict(set)

    def add_edge(self, u, v):

        node_keys = self.nodes.keys()

        if u not in node_keys and v not in node_keys:
            first_node = Node(u)
            second_node = Node(v)
            first_node.children[v] = second_node
            self.nodes[u] = first_node
            self.nodes[v] = second_node

        elif u in node_keys and v not in node_keys:
            first_node = self.nodes[u]
            second_node = Node(v)
            first_node.children[v] = Node(v)
            self.nodes[v] = second_node

        elif u not in node_keys and v in node_keys:
            first_node = self.nodes[v]
            second_node = Node(u)
            second_node.children[v] = first_node
            self.nodes[u] = second_node

    def dfs_util(self, node):
        node.visited = True
        print(node, end=' ')
        for child in node.children:
            child_node = node.children[child]
            if not child_node.visited:
                self.dfs_util(child_node)

    def dfs(self):
        for val in self.nodes:
            node = self.nodes[val]
            if node.visited == False:
                self.dfs_util(node)
            print('\n')

    # def bfs():

def main():
    data_set = sys.stdin.readlines()
    graph = Graph()
    for data in data_set:
        data = list(map(int, data.split()))
        u = data[0]
        v = data[1]
        graph.add_edge(u, v)
    
    graph.dfs()


if __name__ == '__main__':
    main()
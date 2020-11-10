import random
from graph import Graph


def generate_numbers():
    size = random.randint(500, 1000)
    nums1 = [i+1 for i in range(size)]
    nums2 = [random.randint(1,size) for i in range(size)]

    return size, nums1, nums2

def generate_graph(size, nums1, nums2):
    graph = Graph(size)
    for u, v in zip(nums1, nums2):
        graph.add_edge(u, v)
    
    return graph
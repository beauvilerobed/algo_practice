import random
from graph import Graph


def generate_graphs(num_of_graphs=250):
    test_cases = []
    for _ in range(num_of_graphs):
        nums1, nums2 = generate_numbers()
        graph = generate_graph(nums1, nums2)
        test_cases.append((graph, nums1))
    
    return test_cases


def generate_numbers(number=1000):
    size = random.randint(number//10, number)
    nums1 = [i+1 for i in range(size)]
    nums2 = [random.randint(1, size) for i in range(size)]

    return nums1, nums2


def generate_graph(nums1, nums2):
    size = len(nums1)
    graph = Graph(size)
    for u, v in zip(nums1, nums2):
        graph.add_edge(u, v)

    return graph

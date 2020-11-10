import unittest
from generate_graph import generate_numbers, generate_graph


def generate_graphs():
    test_cases = []
    for _ in range(1000):
        size, nums1, nums2 = generate_numbers()
        graph = generate_graph(size, nums1, nums2)
        test_cases.append((graph, nums1))
    
    return test_cases

class TestGraph(unittest.TestCase):
    def test_bfs_method(self):
        test_cases = generate_graphs()
        for graph, answer in test_cases:
            self.assertCountEqual(graph.dfs(), answer)

    def test_dfs_method(self):
        test_cases = generate_graphs()
        for graph, answer in test_cases:
            self.assertCountEqual(graph.dfs(), answer)

    def test_stress(self):
        test_cases = generate_graphs()
        for graph, _ in test_cases:
            self.assertCountEqual(graph.dfs(), graph.bfs())
    

if __name__ == '__main__':
    unittest.main()
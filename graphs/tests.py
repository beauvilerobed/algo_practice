import unittest
from generate_graph import generate_graphs


class TestGraph(unittest.TestCase):
    def test_bfs_method(self):
        test_cases = generate_graphs()
        for graph, answer in test_cases:
            self.assertCountEqual(graph.bfs(), answer)

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

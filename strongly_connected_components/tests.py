import os
from scc import Node, Graph, find_scc
import unittest
from file_reader import generate_files, generate_cases

input_files, output_files = generate_files()
inputs_outputs = generate_cases(input_files, output_files)


class TestSCC(unittest.TestCase):
    def test_cases(self):
        # runtime to process and test files is ~ 25 sec.
        count = 1
        for graph, data in inputs_outputs:
            self.assertEqual(find_scc(graph), data)
            print("passed test case:", count)
            count += 1

if __name__ == '__main__':
    unittest.main()

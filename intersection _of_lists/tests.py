import unittest
from intersection_of_lists import intersection
import random


class ToBinary(unittest.TestCase):
    def test_small(self):
        test_case = [
            ([], ['1', '5', '3'], []),
            (['1', '5', '3'], ['0', '5', '3'], ['5', '3']),
        ]
        for a, b, ans in test_case:
            self.assertEqual(set(intersection(a,b)), set(ans))

if __name__ == '__main__':
    unittest.main()

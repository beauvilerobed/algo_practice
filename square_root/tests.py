import unittest
from square_root import square_root
from math import sqrt
import random

class SquareRoot(unittest.TestCase):
    def test_small(self):
        test_cases = [
            (4, 2.0),
            (9, 3.0),
            (0, 0.0),
        ]
        for n, answer in test_cases:
            self.assertEqual(square_root(n), answer)

    def test_large(self):
        test_cases = [
            (10 ** 7, sqrt(10 ** 7)),
            (2 ** 10, 2 ** 5),
        ]
        for n, answer in test_cases:
            self.assertAlmostEqual(square_root(n), answer)

    def test_stress(self):
        test_cases = [random.randint(0, 10 ** 7) for _ in range(10 ** 5)]
        for n in test_cases:
            # checks that round(a-b, 7) == 0
            self.assertAlmostEqual(square_root(n), n ** .5)
        

if __name__ == '__main__':
    unittest.main()
import unittest
from multiply import multiply
import random

class Multipy(unittest.TestCase):
    def test_small(self):
        test_cases = [
            (4, 2),
            (9, 3),
            (0, 0),
        ]
        for a, b in test_cases:
            self.assertEqual(multiply(a, b), a * b)

    def test_large(self):
        test_cases = [
            (10 ** 3, 10 ** 4),
            (2 ** 10, 2 ** 5),
        ]
        for a, b in test_cases:
            self.assertEqual(multiply(a, b), a * b)

    def test_stress(self):
        test_cases = [(random.randint(-10 ** 5, 10 ** 5), random.randint(-10 ** 5, 10 ** 5)) for _ in range(1000)]
        for a , b in test_cases:
            self.assertEqual(multiply(a, b), a * b)
        

if __name__ == '__main__':
    unittest.main()
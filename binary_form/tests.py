import unittest
from binary_form import to_binary
import random


class ToBinary(unittest.TestCase):
    def test_small(self):
        test_case = [
            (1, '1'),
            (24, '11000'),
            (32, '100000'),
        ]
        for n, answer in test_case:
            self.assertEqual(to_binary(n), answer)

    def test_large(self):
        test_case = [
            (10 ** 6, bin(10 ** 6)[2:]),
            (2 ** 6, '1' + '0' * 6),
        ]
        for n, answer in test_case:
            self.assertEqual(to_binary(n), answer)

    def test_stress(self):
        test_cases = [random.randint(0, 10 ** 5)
                      for _ in range(random.randint(50, 100))]
        for n in test_cases:
            if to_binary(n) != bin(n)[2:]:
                print(n)
            self.assertEqual(to_binary(n), bin(n)[2:])


if __name__ == '__main__':
    unittest.main()

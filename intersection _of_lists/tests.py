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

'''    def test_large(self):
        test_case = [
            (10 ** 6, bin(10 ** 6)[2:]),
            (2 ** 6, '1' + '0' * 6),
        ]
        for a, b, ans in test_case:
            self.assertEqual(set(intersection(a,b)), set(ans))

    def test_stress(self):
        test_cases = [random.randint(0, 10 ** 5)
                      for _ in range(random.randint(50, 100))]
        for a, b, ans in test_case:
            self.assertEqual(set(intersection(a,b)), set(ans))'''


if __name__ == '__main__':
    unittest.main()

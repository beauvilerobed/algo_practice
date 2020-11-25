import unittest
import sys
import random
from remove_even import remove_even, remove_even_naive,\
                        remove_even_less, remove_even_in_place


class RemoveEven(unittest.TestCase):
    def test_small(self):
        test_cases = [
            ([1, 2, 3, 4, 5], [1, 3, 5]),
            ([2, 2, 2, 2, 2], []),
            ([3, 3, 3, 3, 3], [3, 3, 3, 3, 3]),
            ([-10, -11, 0, 0, 0], [-11]),
        ]

        for nums, answer in test_cases:
            self.assertEqual(remove_even(nums), answer)

    def test_large(self):
        test_cases = [
            ([1] * (10 ** 5), [1] * (10 ** 5)),
            ([2] * (10 ** 5), []),
            ([2] * (10 ** 5 - 1) + [1], [1]),
        ]

        for nums, answer in test_cases:
            self.assertEqual(remove_even(nums), answer)

    def test_stress(self):
        test_cases = [[random.randint(1, 1000)
                      for _ in range(100)]
                      for _ in range(1000)]
        for nums in test_cases:
            self.assertEqual(remove_even(nums), remove_even_naive(nums))

    def test_more_stress(self):
        test_cases = [[random.randint(1, 1000)
                      for _ in range(100)]
                      for _ in range(1000)]
        for nums in test_cases:
            self.assertEqual(remove_even(nums), remove_even_less(nums))

    def test_more_more_stress(self):
        test_cases = [[random.randint(1, 1000)
                      for _ in range(100)]
                      for _ in range(1000)]
        for nums in test_cases:
            first = set(remove_even(nums))
            second = set(remove_even_in_place(nums))
            self.assertEqual(first, second)


if __name__ == '__main__':
    unittest.main()

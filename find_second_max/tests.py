import unittest
import random
from numpy import random
from find_second_max import find_second_max, find_second_max_naive


class FindSecondMax(unittest.TestCase):
    def test_small(self):
        test_cases = [
            ([], None),
            ([1, 2, 3, 4], 3),
            ([1, 1, 1, 1], None),
            ([2, 4, 7, 0], 4)
        ]

        for nums, answer in test_cases:
            self.assertEqual(find_second_max(nums), answer)

    def test_large(self):
        test_cases = [
            ([1] * 10 ** 5, None),
            ([i % 2 for i in range(1000)], 0)
        ]
        for nums, answer in test_cases:
            self.assertEqual(find_second_max(nums), answer)

    def test_stress(self):
        number = 1000
        test_cases = random.randint(-number, number, size=(number*10, number//10))
        for nums in test_cases:
            self.assertEqual(find_second_max(nums),
                             find_second_max_naive(nums))


if __name__ == '__main__':
    unittest.main()

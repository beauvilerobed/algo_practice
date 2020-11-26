import unittest
import random
import copy
from sort_values import sort_stack


class SortStack(unittest.TestCase):
    # tests take a total of 10-12 sec
    def test_small(self):
        test_cases = [
            ([2, 3, 1], [1, 2, 3]),
            ([1, 1, 1], [1, 1, 1]),
            ([1, -1, 1, -1], [-1, -1, 1, 1]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
        ]
        for nums, answer in test_cases:
            self.assertEqual(sort_stack(nums), answer)

    def test_large(self):
        test_cases = [
            ([(10 ** 6) - 1 - i for i in range(10 ** 6)],
             [i for i in range(10 ** 6)]),
            ([1] * 10 ** 6, [1] * 10 ** 6),
            ([i % 2 for i in range(10 ** 4)],
             [0 for _ in range(10 ** 4 // 2)] +
             [1 for _ in range(10 ** 4 // 2)])
        ]
        for nums, answer in test_cases:
            self.assertEqual(sort_stack(nums), answer)
            print("passed")

    def test_stress(self):
        test_cases = [[random.randint(1, 1000)
                      for _ in range(random.randint(500, 1000))]
                      for _ in range(random.randint(5, 10))]
        for nums in test_cases:
            new_nums = copy.copy(nums)
            new_nums.sort()
            actual = sort_stack(nums)
            self.assertEqual(actual, new_nums)


if __name__ == '__main__':
    unittest.main()

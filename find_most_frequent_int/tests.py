import unittest
from find_most_frequent import find_most_frequent


class FindMostFrequent(unittest.TestCase):
    def test_small(self):
        test_cases = [
            ([], None),
            ([1, 1, 1, 2, 2, 2], 1),
            ([1, 2, 3, 3], 3),
            ([-2, -1, -4, 5, 5, 5, 6], 5),
        ]
        for nums, answer in test_cases:
            self.assertEqual(find_most_frequent(nums), answer)

    def test_large(self):
        test_cases = [
            ([1] * 10 ** 6 + [2] * (10 ** 6 + 1), 2),
            ([i % 10 for i in range(10000)] + [9], 9),
        ]
        for nums, answer in test_cases:
            self.assertEqual(find_most_frequent(nums), answer)


if __name__ == '__main__':
    unittest.main()
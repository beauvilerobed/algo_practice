import unittest
from binary_search_on_rotation import binary_on_rotation
import random
from generate_rotation import generate_rotations, generate_sorted_nums


class BinarySearch(unittest.TestCase):
    def test_small(self):
        test_cases = [
            ([1, 2, 3, 5], 5, 5),
            ([20, 30, 50, 100, 10], 10, 10),
            ([20, 30, 50, 100, 10], 101, None),
            ([1, 1, 1, 1, 1], 1, 1),
            ([], 10000, None),
        ]
        for nums, target, answer in test_cases:
            self.assertEqual(binary_on_rotation(nums, target), answer)

    def test_large(self):
        test_cases = [
            ([i + 1000 for i in range(10 ** 6)] +
             [i for i in range(1000)], 1001, 1001),
            ([i + 1 for i in range(10 ** 6)] + [0], 0, 0),
        ]
        for nums, target, answer in test_cases:
            self.assertEqual(binary_on_rotation(nums, target), answer)

    def test_stress(self):
        nums = generate_sorted_nums()
        test_cases = generate_rotations(nums)
        for nums in test_cases:
            target = random.randint(-10000, 10000)
            expected = target if target in nums else None
            self.assertEqual(binary_on_rotation(nums, target), expected)


if __name__ == '__main__':
    unittest.main()

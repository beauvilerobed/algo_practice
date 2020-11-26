import unittest
from find_smallest import find_smallest
from find_second_smallest import find_second_smallest
from utils import generate_bsts_and_nums_small, generate_bsts_and_nums,\
    generate_expected_actual, find_second_min


class TestBST(unittest.TestCase):
    def test_small_insert(self):
        bsts, nums = generate_bsts_and_nums_small()
        for vals, bst in zip(nums, bsts):
            string_nums = list(map(str, vals))
            ordered_string = " ".join(string_nums)
            self.assertEqual(ordered_string, str(bst))

    def test_insert(self):
        bsts, nums = generate_bsts_and_nums()
        for vals, bst in zip(nums, bsts):
            string_nums = list(map(str, vals))
            ordered_string = " ".join(string_nums)
            self.assertEqual(ordered_string, str(bst))

    def test_small_delete(self):
        bsts, nums = generate_bsts_and_nums_small()
        expected, actual = generate_expected_actual(bsts, nums)
        for sorted_bst_nums, bst_nums in zip(expected, actual):
            self.assertEqual(sorted_bst_nums, bst_nums)

    def test_delete(self):
        bsts, nums = generate_bsts_and_nums()
        expected, actual = generate_expected_actual(bsts, nums)
        for sorted_bst_nums, bst_nums in zip(expected, actual):
            self.assertEqual(sorted_bst_nums, bst_nums)

    def test_find_smallest(self):
        bsts, nums = generate_bsts_and_nums()
        for nums, bst in zip(nums, bsts):
            minimum = min(nums)
            self.assertEqual(minimum, find_smallest(bst))

    def test_find_second_smallest(self):
        bsts, nums = generate_bsts_and_nums()
        for vals, bst in zip(nums, bsts):
            second_smallest = find_second_min(vals)
            self.assertEqual(second_smallest, find_second_smallest(bst))


if __name__ == '__main__':
    unittest.main()

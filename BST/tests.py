import unittest
from bst import BST
import random
from find_smallest import find_smallest
from find_second_smallest import find_second_smallest


def generate_bsts_and_nums(number=1000):
    bsts_and_nums = []
    random_nums = [[random.randint(-number, number) for
                    _ in range(number)] for _ in range(number//10)]
    for nums in random_nums:
        bst = BST()
        for num in nums:
            bst.insert(num)
        bsts_and_nums.append((nums, bst))

    return bsts_and_nums


class TestBST(unittest.TestCase):
    def test_insert(self):
        bsts_and_nums = generate_bsts_and_nums()
        for nums, bst in bsts_and_nums:
            nums.sort()
            string_nums = list(map(str, nums))
            ordered_string = " ".join(string_nums)
            self.assertEqual(ordered_string, str(bst))

    def test_delete(self):
        bsts_and_nums = generate_bsts_and_nums()
        for nums, bst in bsts_and_nums:
            for num in nums:
                if num % 3 == 0:
                    bst.delete(num)

            num_string = str(bst)
            char_nums = num_string.split()
            bst_nums = list(map(int, char_nums))
            sorted_bst_nums = sorted(bst_nums)
            self.assertEqual(sorted_bst_nums, bst_nums)

    def test_find_smallest(self):
        bsts_and_nums = generate_bsts_and_nums()
        for nums, bst in bsts_and_nums:
            minimum = min(nums)
            self.assertEqual(minimum, find_smallest(bst))

    def test_find_second_smallest(self):
        bsts_and_nums = generate_bsts_and_nums()
        for nums, bst in bsts_and_nums:
            minimum = min(nums)
            nums.remove(minimum)
            minimum = min(nums)
            self.assertEqual(minimum, find_second_smallest(bst))


if __name__ == '__main__':
    unittest.main()

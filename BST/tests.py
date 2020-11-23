import unittest
from bst import BST
import random

def generate_bsts_nums():
    bsts_and_nums = []
    random_nums = [[random.randint(-1000, 1000) for _ in range(random.randint(500, 1000))] for _ in range(random.randint(50, 100))]
    for nums in random_nums:
        bst = BST()
        for num in nums:
            bst.insert(num)
        bsts_and_nums.append((nums, bst))
    
    return bsts_and_nums


class TestBST(unittest.TestCase):
    def test_insert(self):
        bsts_and_nums = generate_bsts_nums()
        for nums, bst in bsts_and_nums:
            nums.sort()
            string_nums = list(map(str, nums))
            ordered_string = " ".join(string_nums)
            self.assertEqual(ordered_string, str(bst))

    def test_delete(self):
        bsts_and_nums = generate_bsts_nums()
        for nums, bst in bsts_and_nums:
            for num in nums:
                if num % 3 == 0:
                    bst.delete(num)

            num_string = str(bst)
            char_nums = num_string.split()
            bst_nums = list(map(int, char_nums))
            sorted_bst_nums = sorted(bst_nums)
            self.assertEqual(sorted_bst_nums, bst_nums)

    # def test_find_smallest(self):


    # def test_find_second_smallest(self):


if __name__ == '__main__':
    unittest.main()

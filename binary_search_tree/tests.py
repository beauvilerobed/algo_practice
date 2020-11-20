import unittest
from bst import BST
import random


class TestBST(unittest.TestCase):
    def test_insert(self):
        test_case = [[random.randint(-1000, 1000) for _ in range(random.randint(500, 1000))] for _ in range(random.randint(500, 1000))]
        for nums in test_case:
            bst = BST()
            for num in nums:
                bst.insert(num)

            nums.sort()
            ordered_string = ''
            for num in nums:
                ordered_string += " " + str(num)
            
            self.assertEqual(ordered_string, str(bst))


if __name__ == '__main__':
    unittest.main()
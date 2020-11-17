import unittest
from min_stack import MinStack
import random

class TestMinStack(unittest.TestCase):
    def test_add_and_pop_method(self):
        test_case = [[random.randint(-1000, 1000) for _ in range(random.randint(0, 1000))] for _ in range(random.randint(1, 1000))]
        for nums in test_case:
            stack = MinStack()
            array = []
            n = len(nums)
            for i in range(n):
                stack.add(nums[n - i - 1])

            for _ in range(len(nums)):
                val = stack.pop()
                array.append(val)

            self.assertEqual(array, nums)
    
    def test_minimum_val_method(self):
        test_case = [[random.randint(-1000, 1000) for _ in range(random.randint(1, 1000))] for _ in range(random.randint(1, 1000))]
        for nums in test_case:
            stack = MinStack()
            n = len(nums)
            for i in range(n):
                stack.add(nums[i])
            
            expected = min(nums)
            actual = stack.minimum_val()
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
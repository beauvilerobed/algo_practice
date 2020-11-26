import unittest
import random
from numpy import random
from bubble_sort import bubble_sort


class BubbleSort(unittest.TestCase):
    def test_small(self):
        test_case = [
            ([2, 1, 1], [1, 1, 2]),
            ([2, 3, 0], [0, 2, 3]),
            ([], []),
            ([4, 3, 2, 1, 9, 7, 6, 0], [0, 1, 2, 3, 4, 6, 7, 9]),
        ]
        for nums, answer in test_case:
            self.assertEqual(bubble_sort(nums), answer)

    def test_large(self):
        test_case = [
            ([10 ** 3 - 1 - k for k in range(10 ** 3)],
                [k for k in range(10 ** 3)]),
        ]
        for nums, answer in test_case:
            self.assertEqual(bubble_sort(nums), answer)

    def test_stress(self):
        # 500 gives bubble runtime to be around 2-3 sec
        number = 500
        test_cases = random.randint(-number, number, size=(number//10, number))
        for nums in test_cases:
            answer = sorted(nums)
            self.assertEqual(bubble_sort(nums), answer)


if __name__ == '__main__':
    unittest.main()

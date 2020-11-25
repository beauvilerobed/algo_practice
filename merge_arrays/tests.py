import unittest
import random
from merge_array import merge_array, merge_array_naive


class MergeArray(unittest.TestCase):
    def test_small(self):
        test_cases = [
            ([1], [2], [1, 2]),
            ([1], [1], [1, 1]),
            ([1, 2, 3, 4], [5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
            ([1, 2, 7, 7, 10], [3, 5, 7], [1, 2, 3, 5, 7, 7, 7, 10])
        ]

        for nums1, nums2, answer in test_cases:
            self.assertEqual(merge_array(nums1, nums2), answer)

    def test_large(self):
        test_cases = [
            ([1 for i in range(100)], [0 for i in range(1000)],
             [0 for i in range(1000)]+[1 for i in range(100)]),
            ([1] * 10 ** 5, [7], [1] * 10 ** 5 + [7])
        ]
        for nums1, nums2, answer in test_cases:
            self.assertEqual(merge_array(nums1, nums2), answer)

    def test_stress(self):
        test_cases = []
        for _ in range(10000):
            temp = [random.randint(1, 1000)
                    for _ in range(random.randint(50, 100))]
            temp.sort()
            test_cases.append(temp)

        for i in range(0, 1000, 2):
            nums1 = test_cases[i]
            nums2 = test_cases[i + 1]
            self.assertEqual(merge_array(nums1, nums2),
                             merge_array_naive(nums1, nums2))


if __name__ == '__main__':
    unittest.main()

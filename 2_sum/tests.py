import unittest
from two_sum import two_sum
from numpy import random


def reference(nums, target):
    nums = sorted(nums)
    n = len(nums)
    left = 0
    right = n - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return nums[left], nums[right]

        if nums[left] + nums[right] < target:
            left += 1

        if nums[left] + nums[right] > target:
            right -= 1
    return None


class TwoSum(unittest.TestCase):
    def test_small(self):
        test_cases = [
            ([1, 2, 3, 5, 5, 6], (5, 5)),
            ([-1, -2, 3, 3], None),
            ([4, 5, 0, 0, 6], (4, 6)),
        ]
        for nums, answer in test_cases:
            self.assertEqual(two_sum(nums, 10), answer)

    def test_large(self):
        test_cases = [
            ([10] * 10 ** 6, None),
            ([5] * 10 ** 6, (5, 5)),
            ([1] * 10 ** 6, None),
        ]
        for nums, answer in test_cases:
            self.assertEqual(two_sum(nums, 10), answer)

    def test_stress(self):
        num = 1000
        test_cases = random.randint(-num, num, size=(num, num // 2))
        for nums in test_cases:
            actual = sum(two_sum(nums, 10)) if two_sum(nums, 10) else None
            expected = sum(reference(nums, 10)) if reference(nums, 10) else None
            if actual != expected:
                print(nums)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

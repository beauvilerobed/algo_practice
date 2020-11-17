import unittest
from is_cycle import LinkedList, is_cycle
from find_cycle import find_cycle
import random


class FindCycle(unittest.TestCase):
    def test_is_cycle(self):
        test_cases = [[random.randint(-1000, 1000) for _ in range(random.randint(1, 1000))] for _ in range(random.randint(1, 1000))]
        for nums in test_cases:
            nums_set = set(nums)
            yes = 0
            no = -1
            answer = no if len(nums) == len(nums_set) else yes
            linklist = LinkedList()

            for i in range(len(nums)):
                linklist.add(nums[i])

            if answer == yes:
                linklist.add_cycle()

            actual = is_cycle(linklist)
            self.assertEqual(actual, answer)

    def test_find_cycle(self):
        test_cases = [[random.randint(-1000, 1000) for _ in range(random.randint(1, 100))] for _ in range(random.randint(1, 100))]
        for nums in test_cases:
            nums_set = set(nums)
            yes = 0
            no = -1
            answer = no if len(nums) == len(nums_set) else yes
            expected = nums[0]

            linklist = LinkedList()

            for i in range(len(nums)):
                linklist.add(nums[i])

            if answer == yes:
                linklist.add_cycle()
            else:
                expected = 'no cycle'

            actual = find_cycle(linklist)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
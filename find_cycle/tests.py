import unittest
from linked_list import LinkedList
from is_cycle import is_cycle
from find_cycle import find_cycle
import random


class FindCycle(unittest.TestCase):
    def test_is_cycle(self):
        test_cases = [[random.randint(-1000, 1000)
                      for _ in range(random.randint(1, 10000))]
                      for _ in range(random.randint(1, 1000))]
        for nums in test_cases:
            nums_set = list(set(nums))
            yes = 0
            no = -1
            answer_is_cycle = no if len(nums) == len(nums_set) else yes
            linklist = LinkedList()

            # we need all values to be unique,
            # then we add the cylce below to test
            nums = nums_set
            for i in range(len(nums)):
                linklist.add(nums[i])

            if answer_is_cycle == yes:
                linklist.add_cycle()

            actual = is_cycle(linklist)
            self.assertEqual(actual, answer_is_cycle)

    def test_find_cycle(self):
        test_cases = [[random.randint(-1000, 1000)
                      for _ in range(random.randint(1, 10000))]
                      for _ in range(random.randint(1, 100))]
        for nums in test_cases:
            nums_set = list(set(nums))
            yes = 0
            no = -1
            answer_is_cycle = no if len(nums) == len(nums_set) else yes

            linklist = LinkedList()

            # we need all values to be unique,
            # then we add the cylce below to test if it can be found
            nums = nums_set
            for i in range(len(nums)):
                linklist.add(nums[i])

            if answer_is_cycle == yes:
                linklist.add_cycle()
                expected = nums[0]
            else:
                expected = 'no cycle'

            actual = find_cycle(linklist)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

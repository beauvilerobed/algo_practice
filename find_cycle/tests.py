import unittest
from linked_list import LinkedList
from is_cycle import is_cycle
from find_cycle import find_cycle
from numpy import random


def return_expected(nums):
    return "no" if len(nums) == len(set(nums)) else "yes"


def return_linklist(nums):
    linklist = LinkedList()
    for i in range(len(nums)):
        linklist.add(nums[i])

    return linklist


class FindCycle(unittest.TestCase):
    # test takes total of 3 - 4 sec
    def test_is_cycle(self):
        number = 1000
        rand_nums = random.randint(-number, number, size=(number, number))
        for nums in rand_nums:
            expected = return_expected(nums)
            nums = list(set(nums))
            linklist = return_linklist(nums)

            if expected == "yes":
                linklist.add_cycle()

            actual = is_cycle(linklist)
            self.assertEqual(actual, expected)

    def test_find_cycle(self):
        number = 1000
        rand_nums = random.randint(-number, number, size=(number, number))
        for nums in rand_nums:
            expected = return_expected(nums)
            nums = list(set(nums))
            linklist = return_linklist(nums)

            if expected == "yes":
                linklist.add_cycle()
                expected = nums[0]
            else:
                expected = 'no cycle'

            actual = find_cycle(linklist)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

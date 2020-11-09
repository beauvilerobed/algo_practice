import unittest
import random
from linked_list import LinkedList


def generate_linkedlists_and_arrays(number=1000):
    arrays = [[random.randint(1, number) for _ in range(1, number)] for _ in range(number)]
    linklists = []
    for nums in arrays:
        linklist = LinkedList()
        for num in nums:
            linklist.add(num)

    return linklists, arrays

class TestLinkedList(unittest.TestCase):
    def test_reverse_method(self):
        linklist, arrays = generate_linkedlists_and_arrays()
        for linklist, nums in zip(linklist, arrays):
            self.assertEqual(linklist.reverse(), nums)

    def test_search_method(self):
        linklist, arrays = generate_linkedlists_and_arrays()
        n = random.randint(1, 1000)
        for linklist, nums in zip(linklist, arrays):
            result = ''
            if n in nums:
                result = "success"
            else:
                result = "failure"
            self.assertEqual(linklist.search(n), result)

    def test_len_method(self):
        linklist, arrays = generate_linkedlists_and_arrays()
        for linklist, nums in zip(linklist, arrays):
            self.assertEqual(len(linklist), len(nums))

    def test_middle_method(self):
        linklist, arrays = generate_linkedlists_and_arrays()
        for linklist, nums in zip(linklist, arrays):
            n = len(nums)
            self.assertEqual(linklist.middle(), nums[n // 2 - 1])


if __name__ == '__main__':
    unittest.main()
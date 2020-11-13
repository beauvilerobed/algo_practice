import unittest
import random
from linked_list import LinkedList


def generate_linkedlists_and_arrays(number=500):
    arrays = [[random.randint(1, number) for _ in range(1, number)] for _ in range(number)]
    linklists = []
    for nums in arrays:
        linklist = LinkedList()
        n = len(nums)
        for i in range(n):
            linklist.add(nums[n-i-1])
        linklists.append(linklist)

    return linklists, arrays

class TestLinkedList(unittest.TestCase):
    def test_reverse_method(self):
        linklists, arrays = generate_linkedlists_and_arrays()
        for linklist, nums in zip(linklists, arrays):
            self.assertEqual(linklist.return_array(), nums)

    def test_search_method(self):
        linklists, arrays = generate_linkedlists_and_arrays()

        assert len(linklists) > 0 and len(arrays) > 0

        n = random.randint(1, 1000)
        for linklist, nums in zip(linklists, arrays):
            result = ''
            if n in nums:
                result = "success"
            else:
                result = "failure"
            self.assertEqual(linklist.search(n), result)

    def test_len_method(self):
        linklists, arrays = generate_linkedlists_and_arrays()

        assert len(linklists) > 0 and len(arrays) > 0

        for linklist, nums in zip(linklists, arrays):
            self.assertEqual(len(linklist), len(nums))

    def test_middle_method(self):
        linklists, arrays = generate_linkedlists_and_arrays()

        assert len(linklists) > 0 and len(arrays) > 0   

        for linklist, nums in zip(linklists, arrays):
            m = len(nums)
            self.assertEqual(linklist.middle(), nums[m // 2])

    def test_remove_method(self):
        linklists, arrays = generate_linkedlists_and_arrays()

        assert len(linklists) > 0 and len(arrays) > 0  

        for linklist, nums in zip(linklists, arrays):
            n = len(nums)
            del nums[n // 2 - 1]
            linklist.remove(n // 2 - 1)
            self.assertEqual(linklist.return_array(), nums)

    def test_search_nth_method(self):
        linklists, arrays = generate_linkedlists_and_arrays()

        assert len(linklists) > 0 and len(arrays) > 0  

        for linklist, nums in zip(linklists, arrays):
            n = len(nums)
            m = random.randint(-n, -n) 
            result = nums[m] if 0 <= m and m <= n -1 else "doesn't exist"
            self.assertEqual(linklist.search_nth(m), result)


if __name__ == '__main__':
    unittest.main()
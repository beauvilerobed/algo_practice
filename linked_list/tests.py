import unittest
import random
import math
from linked_list import LinkedList
from generate_linked_lists import generate_linkedlists_and_arrays, generate_linkedlists_and_palindromes
from check_if_palindrome import is_palindrome


class TestLinkedList(unittest.TestCase):
    def test_reverse_method(self):
        linklists, arrays = generate_linkedlists_and_arrays()

        assert len(linklists) > 0 and len(arrays) > 0

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
        linklists, arrays = generate_linkedlists_and_arrays(10)

        assert len(linklists) > 0 and len(arrays) > 0   

        for linklist, nums in zip(linklists, arrays):
            m = len(nums) - 1
            result = "empty linked list"
            if m > -1:
                result = nums[m // 2]
            self.assertEqual(linklist.middle(), result)

    def test_remove_method(self):
        linklists, arrays = generate_linkedlists_and_arrays()

        assert len(linklists) > 0 and len(arrays) > 0  

        for linklist, nums in zip(linklists, arrays):
            n = random.randint(-1000, 1000)
            m = len(nums)
            result = nums
            if 0 <= n < m:
                del nums[n]
                result = nums
            linklist.remove(n)
            self.assertEqual(linklist.return_array(), result)

    def test_search_nth_method(self):
        linklists, arrays = generate_linkedlists_and_arrays()

        assert len(linklists) > 0 and len(arrays) > 0  

        for linklist, nums in zip(linklists, arrays):
            n = len(nums)
            m = random.randint(-n, -n) 
            result = nums[m] if 0 <= m and m <= n -1 else "doesn't exist"
            self.assertEqual(linklist.search_nth(m), result)
    
    def test_is_palindrome(self):
        linklists, arrays = generate_linkedlists_and_palindromes()

        assert len(linklists) > 0 and len(arrays) > 0  

        for linklist, nums in zip(linklists, arrays):
            result = "no"
            if nums == nums[::-1]:
                result = "yes"
            self.assertEqual(is_palindrome(linklist), result)


if __name__ == '__main__':
    unittest.main()
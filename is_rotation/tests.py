import unittest
from is_rotation import is_rotation
from generate_rotation import generate_nums, generate_rotations


def reference(array1, array2):
    array2 += array2
    flag = -1
    if(all(x in array2 for x in array1)): 
        flag = 0
    return flag
    

class IsRotation(unittest.TestCase):
    def test_small(self):
        test_cases = [
            ([1,2,3,4,5], [4,5,1,2,3], 0),
            ([0,1,2,3,0], [0,1,1,2,3], -1),
            ([],[], 0),
            ([1,2,3], [3,2,1,0], -1),
            (['a','b','c'], ['c','a','b'], 0),
            ([1,1,1], [1,1,1], 0),
        ]
        for array1, array2, answer in test_cases:
            self.assertEqual(is_rotation(array1, array2), answer)

    def test_large(self):
        test_cases = [
            ([1] * 10 ** 5 + [2] * 10 ** 5, [2] * 10 ** 5 + [1] * 10 ** 5, 0),
            ([1] * 10 ** 5 + [2], [1] * 10 ** 5, -1),
            ([1] * 10 ** 5, [2] * 10 ** 5, -1),
        ]
        for array1, array2, answer in test_cases:
            self.assertEqual(is_rotation(array1, array2), answer)
    
    def test_stress(self):
        nums = generate_nums()
        test_cases = generate_rotations(nums)
        for array1, array2 in zip(nums, test_cases):
            self.assertEqual(is_rotation(array1, array2), reference(array1, array2))


if __name__ == '__main__':
    unittest.main()
import unittest
import random
from reverse_string import reverse_recursive, reverse_iterative


class Revers(unittest.TestCase):
    def test_small_itr(self):
        test_cases = [
            ('', ''),
            ('abcd', 'dcba'),
            ('aaaaaaa', 'aaaaaaa'),
            ('a', 'a')
        ]
        for string, answer in test_cases:
            self.assertEqual(reverse_iterative(string), answer)

    def test_small_rec(self):
        test_cases = [
            ('', ''),
            ('abcd', 'dcba'),
            ('aaaaaaa', 'aaaaaaa'),
            ('a', 'a')
        ]
        for string, answer in test_cases:
            self.assertEqual(reverse_recursive(string), answer)

    def test_large_itr(self):
        test_cases = [
            ('l' * 10 ** 6 + 'a', 'a' + 'l' * 10 ** 6),
            ('abc' * 10 ** 5, 'cba' * 10 ** 5),
        ]
        for string, answer in test_cases:
            self.assertEqual(reverse_iterative(string), answer)

    def test_large_rec(self):
        test_cases = [
             ('l' * 10 ** 3 + 'a', 'a' + 'l' * 10 ** 3),
            ('abc' * 10 ** 2, 'cba' * 10 ** 2),
        ]
        for string, answer in test_cases:
            self.assertEqual(reverse_recursive(string), answer)
    
    def test_stress_rec(self):
        test_cases = []
        for _ in range(random.randint(50,1000)):
            values1 = [str(random.randint(1, 1000)) for _ in range(random.randint(50, 100))]
            values1 = "".join(values1)
            values2 = values1[::-1]
            values = (values1, values2)
            test_cases.append(values)
        for string, answer in test_cases:
            self.assertEqual(reverse_recursive(string), answer)
    
    def test_stress_itr(self):
        test_cases = []
        for _ in range(random.randint(50,1000)):
            values1 = [str(random.randint(1, 1000)) for _ in range(random.randint(50, 1000))]
            values1 = "".join(values1)
            values2 = values1[::-1]
            values = (values1, values2)
            test_cases.append(values)
        for string, answer in test_cases:
            self.assertEqual(reverse_iterative(string), answer)



if __name__ == '__main__':
    unittest.main()
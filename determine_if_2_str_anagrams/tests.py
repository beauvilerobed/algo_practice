import unittest
import random
from determine_if_anagram import check_if_anagram, check_if_anagram_naive


class Anagram(unittest.TestCase):
    def test_small(self):
        test_cases = [
            ('abcde', 'bacde', 0),
            ('11111', '111', -1),
            ('jahkjfhd', 'bacakjkjde', -1),
        ]
        for string1, string2, answer in test_cases:
            self.assertEqual(check_if_anagram(string1, string2), answer)

    def test_large(self):
        test_cases = [
            ('1234' * 10 ** 6, '4312' * 10 ** 6, 0),
            ('1' * 10 ** 6, '1' * (10 ** 6 - 1), -1),
        ]
        for string1, string2, answer in test_cases:
            self.assertEqual(check_if_anagram(string1, string2), answer)

    def test_stress(self):
        test_cases = []
        number = 1000
        for _ in range(random.randint(number//100, number)):
            values = [str(random.randint(1, number))
                      for _ in range(random.randint(number//100, number))]
            string = "".join(values)
            test_cases.append(string)

        for i in range(0, len(test_cases) - 1, 2):
            string1 = test_cases[i]
            string2 = test_cases[i+1]
            self.assertEqual(check_if_anagram(string1, string2),
                             check_if_anagram_naive(string1, string2))


if __name__ == '__main__':
    unittest.main()

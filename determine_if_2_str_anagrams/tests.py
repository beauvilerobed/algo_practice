import unittest
import random
import string
from determine_if_anagram import check_if_anagram, check_if_anagram_naive


def generate_strings(number=1000):
    letter = string.ascii_lowercase
    strings = []
    other_stings = []
    for i in range(number):
        rand_number = random.randint(0, number)
        string1 = ''.join(random.choice(letter) for _ in range(rand_number))
        if i % 2 == 0:
            strings.append(string1 + string1[::-1])
            other_stings.append(string1 + string1[::-1])
        else:
            strings.append(string1)
            other_stings.append("notanagram")
    
    return strings, other_stings


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
        strings, other_stings = generate_strings()
        for string1, string2 in zip(strings, other_stings):
            self.assertEqual(check_if_anagram(string1, string2),
                             check_if_anagram_naive(string1, string2))


if __name__ == '__main__':
    unittest.main()

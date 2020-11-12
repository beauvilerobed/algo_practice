import unittest
import random
from parse_int import parse_int


class ParseInt(unittest.TestCase):
    def test_small(self):
        test_cases = [
            ('', None),
            ('123', 123),
            ('1001', 1001),
            ('0012', 12)
        ]
        for string, answer in test_cases:
            self.assertEqual(parse_int(string), answer)

    def test_large(self):
        test_cases = [
            ('1' * 10 ** 5, int('1' * 10 ** 5)),
            ([str(i % 10) for i in range(10 ** 5)], int("".join([str(i % 10) for i in range(10 ** 5)]))),
        ]
        for string, answer in test_cases:
            self.assertEqual(parse_int(string), answer)

    def test_stress(self):
        test_cases = [str(random.randint(0, 10 ** 5)) for _ in range(1000)]
        for string in test_cases:
            self.assertEqual(parse_int(string), int(string))


if __name__ == '__main__':
    unittest.main()
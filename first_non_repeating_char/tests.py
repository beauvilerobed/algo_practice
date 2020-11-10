import unittest
from first_non_repeating import find_non_repeating


class FindNoneRepeating(unittest.TestCase):
    def test_small(self):
        test_case = [
            ('hello', 1),
            ('hheelloow', 9),
            ('hheelloohh', -1),
            ('hheeclloohh', 5),
            ('', -1),
        ]
        for string, answer in test_case:
            self.assertEqual(find_non_repeating(string), answer)

    def test_large(self):
        test_case = [
            ('l' * 10 ** 3 , -1),
            ('l' * 10 ** 3 + 'a' + 'l' * 10 ** 3, 10 ** 3 + 1),
        ]
        for string, answer in test_case:
            self.assertEqual(find_non_repeating(string), answer)



if __name__ == '__main__':
    unittest.main()
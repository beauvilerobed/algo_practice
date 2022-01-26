import unittest
from two_sums import find_two_sum_total
from file_reader import generate_files, generate_cases



input_files, output_files = generate_files()
cases = generate_cases(input_files, output_files)
targets = [i for i in range(-10000, 10001)]


class TestTwoSums(unittest.TestCase):
    #TODO: takes ~ 1 min for first 35 cases but then runs really slower(~20 min for first 45 cases), possible solution is nose...
    def test_cases(self):
        count = 1
        for input_value, output_value in cases:
            self.assertEqual(find_two_sum_total(input_value, targets),
                             output_value)
            print("passed test case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()

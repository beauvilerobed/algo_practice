# python3

# Your task is to determine which of the 6 instances are satisfiable, and which 
# are unsatisfiable. In the box below, enter a 6-bit string, where the ith bit 
# should be 1 if the ith instance is satisfiable, and 0 otherwise. For example, 
# if you think that the first 3 instances are satisfiable and the last 3 are not, 
# then you should enter the string 111000 in the box below. 


from file_reader import read_file, reduce_size
from is_true import is_true
from math import log2
from random import choice


def two_sat(clauses, n):
    length = len(clauses)
    for _ in range(int(log2(length))):
        bools = [True]+[choice([True, False]) for _ in range(n)]
        for _ in range(2 * length ** 2):
            for j in range(length):
                if not is_true(clauses, j, bools):
                    break
            if is_true(clauses, j, bools):
                return 1
            else:
                chosen = choice([clauses[j].left, clauses[j].right])
                bools[abs(chosen)] = not bools[abs(chosen)]

    return 0


def main():
    clauses, n = read_file('2sat1.txt')
    clauses = reduce_size(clauses)
    print(two_sat(clauses, n))
    clauses, n = read_file('2sat2.txt')
    clauses = reduce_size(clauses)
    print(two_sat(clauses, n))
    clauses, n = read_file('2sat3.txt')
    clauses = reduce_size(clauses)
    print(two_sat(clauses, n))
    clauses, n = read_file('2sat4.txt')
    clauses = reduce_size(clauses)
    print(two_sat(clauses, n))
    clauses, n = read_file('2sat5.txt')
    clauses = reduce_size(clauses)
    print(two_sat(clauses, n))
    clauses, n = read_file('2sat6.txt')
    clauses = reduce_size(clauses)
    print(two_sat(clauses, n))


if __name__ == '__main__':
    main()

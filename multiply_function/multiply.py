# pyhton3

# task: Write a multiply function that multiples 2 
# integers without using the * symbol

import sys


def multiply(a, b):
    result = 0

    for _ in range(a):
        result += b
    
    return result


def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    a = nums[0]
    b = nums[1]
    print(multiply(a, b))


if __name__ == '__main__':
    main()
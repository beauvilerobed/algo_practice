# python3

# task: Write a function that prints out the binary 
# form of an int


from math import floor, log2

def to_binary(n):
    if n == 0:
        return 0
    array = [None] * (n + 1)

    array[0] = '0'
    array[1] = '1'

    for i in range(2, n + 1):
        k = int(floor(log2(i)))
        num = 2 ** k
        remainder = i - num
        prev_bin = array[remainder]
        p = len(prev_bin)
        m = k - p
        binary = '1' + '0' * m + prev_bin
        array[i] = binary
    
    return array[-1]


def main():
    n = int(input())
    print(to_binary(n))


if __name__ == '__main__':
    main()


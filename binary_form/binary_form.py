# python3

# task: Write a function that prints out the binary 
# form of an int


from math import floor, log2


def to_binary(n):
    if n == 0:
        return 0

    binary_string = '1'

    k = floor(log2(n)) 
    r = n - 2 ** k

    while r > 0:
        nxt = floor(log2(r))
        for _ in range(k - nxt - 1):
            binary_string += '0'
        k = nxt
        binary_string += '1'
        r = r - 2 ** k
    
    for _ in range(k):
        binary_string += '0'
        
    return binary_string


def main():
    n = int(input())
    print(to_binary(n))


if __name__ == '__main__':
    main()

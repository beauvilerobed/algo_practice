# python3

# task: Write a function that prints out the binary 
# form of an int


from math import floor, log2

def to_binary(n):
    if n == 0:
        return 0

    k = floor(log2(n))   
    array = ['1'] + ['0'] * k

    r = n - 2 ** k

    while r > 0:
        k = floor(log2(r))
        array[-(k+1)] = '1'
        r = r - 2 ** k
    
    return "".join(array)


def main():
    n = int(input())
    print(to_binary(n))


if __name__ == '__main__':
    main()


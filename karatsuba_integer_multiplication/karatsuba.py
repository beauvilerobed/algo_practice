# python3

# Implement one or more of the integer multiplication algorithms.
# You'll want to implement recursive integer multiplication and/or Karatsuba's
# algorithm.

# So: what's the product of the following two 64-digit numbers?

# 3141592653589793238462643383279502884197169399375105820974944592

# 271828182845904523536028747135266249775724709369995957496696762`

def karatsuba(strnum1, strnum2):
    num1 = int(strnum1)
    num2 = int(strnum2)

    if num1 < 10 or num2 < 10:
        return num1 * num2

    maxlen = max(len(str(num1)), len(str(num2))) // 2
    base = 10 ** maxlen

    def decompose(num):
        return num // base, num % base

    a, b = decompose(num1)
    c, d = decompose(num2)

    first = karatsuba(a, c)
    second = karatsuba(b, d)
    third = karatsuba(a + b, c + d)

    return first * (base ** 2) + second + base * (third - first - second)


def main():
    first_number = int(input())
    second_number = int(input())
    print(karatsuba(first_number, second_number))


if __name__ == '__main__':
    main()

# python3

# Given a list A of non-negative integers, find the maximum product 
# of two distinct elements (that is, the maximum value of 
# A[i] × A[j] where i ≠ j; note that it may be the case that 
# A[i] = A[j]. The length of A is at least 2 and at most 
# 2 × 105 , all elements are non-negative and do not exceed 
# 2 × 105

def max_pairwise_product_naive(numbers):
    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    first = -float("inf")
    second = -float("inf")
    first_index = int()
    second_index = int()

    # find the first largest value
    for i in range(len(numbers)):
        if numbers[i] > first:
            first = numbers[i]
            first_index = i

    # find the second largest value different from the first
    for j in range(len(numbers)):
        if numbers[j] > second and j != first_index:
            second = numbers[j]
            second_index = j

    return numbers[first_index] * numbers[second_index]


def main():
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))


if __name__ == '__main__':
    main()

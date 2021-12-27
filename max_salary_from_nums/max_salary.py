# python3
 
# As the last question of an interview, your future boss 
# gives you a few pieces of paper with a single number written 
# on each of them and asks you to compose a largest number 
# from these numbers. The resulting number is going to be your 
# salary, so you are very motivated to solve this problem!

# Input: Integers 1 ≤ a1, a_2, ..., an ≤ 103, where 1 ≤ n ≤ 100.

# Output: The largest number that can be composed out of a1, ..., an.


from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(nums):

    for _ in range(len(nums)):
        for i in range(len(nums) - 1):
            # concatenate each letter and it's neighbor and compare
            # the concatenation of each neighbor and the letter
            first_value = int(str(nums[i]) + str(nums[i+1]))
            second_value = int(str(nums[i+1]) + str(nums[i]))
            if first_value < second_value:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    nums = list(map(str, nums))

    return int("".join(nums))


def main():
    n = int(input())
    input_numbers = input().split()
    print(n)
    print(largest_number(input_numbers))


if __name__ == '__main__':
    main()

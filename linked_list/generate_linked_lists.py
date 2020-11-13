import random
from linked_list import LinkedList


def generate_linkedlists_and_arrays(number=500):
    arrays = [[random.randint(0, number) for _ in range(random.randint(0, number))] for _ in range(number)]
    linklists = []
    for nums in arrays:
        linklist = LinkedList()
        n = len(nums)
        for i in range(n):
            linklist.add(nums[n-i-1])
        linklists.append(linklist)

    return linklists, arrays


def generate_linkedlists_and_palindromes(number=500):
    arrays = [[random.randint(1, number) for _ in range(1, number)] for _ in range(number)]

    for i in range(len(arrays)):
        if i % 2 == 0:
            reversed_array = arrays[i][::-1]
            arrays[i] += reversed_array

    linklists = []
    for nums in arrays:
        linklist = LinkedList()
        n = len(nums)
        for i in range(n):
            linklist.add(nums[n-i-1])
        linklists.append(linklist)

    return linklists, arrays
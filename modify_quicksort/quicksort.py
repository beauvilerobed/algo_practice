# python3

# Modify the given implementation of the QuickSort algorithm 
# so that it works fast even on sequences containing many 
# identical elements.


from random import randint


def partition(array, left, right):
    x = array[left]
    start = left
    finish = left
    for j in range(left + 1, right + 1):
        # move the pivot x in front of any value that is less that it
        if array[j] < x:
            y = array[j]
            array[j] = array[finish + 1]
            array[finish + 1] = array[start]
            array[start] = y
            start += 1
            finish += 1
        # if jth value is x then move it to a position next to x
        # and increment the finish index
        elif array[j] == x:
            array[finish + 1], array[j] = array[j], array[finish + 1]
            finish += 1

    return start, finish


def randomized_quick_sort(array, left, right):
    if left < right:
        k = randint(left, right)
        array[left], array[k] = array[k], array[left]
        start, finish = partition(array, left, right)
        randomized_quick_sort(array, left, start - 1)
        randomized_quick_sort(array, finish + 1, right)


def main():
    input_n = int(input())
    elements = list(map(int, input().split()))
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(input_n)
    print(*elements)


if __name__ == '__main__':
    main()

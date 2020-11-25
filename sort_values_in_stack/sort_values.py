# python3

# task: sort values in stack (only using stack operations)

import sys


def sort_stack(stack):
    if len(stack) < 2:
        return stack

    result = []
    first_val = stack.pop(0)
    result.append(first_val)

    while len(stack) > 0:
        temp = stack.pop()
        while len(result) > 0 and temp < result[-1]:
            val = result.pop()
            stack.append(val)

        result.append(temp)

    return result


def main():
    data = sys.stdin.readline()
    data = list(map(int, data.split()))
    print(sort_stack(data))


if __name__ == '__main__':
    main()

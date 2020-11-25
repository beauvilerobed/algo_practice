# python3

# determine if a linked list has a cycle

import sys
from linked_list import LinkedList


def is_cycle(linklist):
    if linklist.head is None:
        return -1

    fast = linklist.head
    slow = linklist.head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if fast.val == slow.val:
            return 0

    return -1


def main():
    data = sys.stdin.readline()
    vals = list(map(int, data.split()))
    linklist = LinkedList()
    for val in vals:
        linklist.add(val)
        linklist.add_cycle()

    print(is_cycle(linklist))
    print(linklist)


if __name__ == '__main__':
    main()

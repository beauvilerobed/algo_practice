# python3

# Determine where the cycle occurs in a cirular linked list

import sys
from linked_list import LinkedList


def find_cycle(linklist):
    if linklist.head is None:
        return "no cycle"

    fast = linklist.head
    slow = linklist.head
    is_cycle = -1

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if fast.val == slow.val:
            is_cycle = 0
            break

    if is_cycle == -1:
        return "no cycle"

    slow = linklist.head

    while slow.next and fast.next:
        if slow.val == fast.val:
            return slow.val
        slow = slow.next
        fast = fast.next


def main():
    data = sys.stdin.readline()
    vals = list(map(int, data.split()))
    linklist = LinkedList()
    for val in vals:
        linklist.add(val)

    linklist.add_cycle()

    print(find_cycle(linklist))
    print(linklist)


if __name__ == '__main__':
    main()

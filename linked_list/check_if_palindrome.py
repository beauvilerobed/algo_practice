# python3

import sys
from linked_list import LinkedList


def is_palindrome(linklist):
    slow = linklist.head
    fast = linklist.head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    while slow.next:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    slow.next = prev

    node = linklist.head

    while slow.next and node.next:
        if slow.value != node.value:
            return "no"
        slow = slow.next
        node = node.next
    
    return "yes"


def main():
    data = sys.stdin.readline()
    data = data.rstrip().split()
    linklist = LinkedList()
    for info in data:
        linklist.add(info)
    print(is_palindrome(linklist))


if __name__ == '__main__':
    main()
    
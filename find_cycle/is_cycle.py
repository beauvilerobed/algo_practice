# python3

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add(self, val):
        self.length += 1
        node = Node(val)

        if self.head is None:
            self.tail = node

        node.next = self.head
        self.head = node

    def add_cycle(self):
        self.length += 1
        node = self.tail
        node.next = self.head
        self.head = node

    def __repr__(self):
        if self.head is None:
            return ""

        string = ""
        node = self.head
        n = self.length
        for _ in range(n + 1):
            if node:
                val = str(node.val)
                string = val + " " + string
                node = node.next

        return string


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

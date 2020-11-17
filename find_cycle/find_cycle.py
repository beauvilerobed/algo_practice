# python3

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def add(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def __repr__(self):
        if self.head is None:
            return ""

        string = ""
        node = self.head
        while node:
            val = str(node.val)
            string = val + " " + string
            node = node.next

        return string


def find_cycle(linklist):
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
    
    print(find_cycle(linklist))
    print(linklist)


if __name__ == '__main__':
    main()

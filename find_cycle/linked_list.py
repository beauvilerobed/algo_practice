# python3


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
        for _ in range(n):
            if node:
                val = str(node.val)
                string = val + " " + string
                node = node.next

        return string
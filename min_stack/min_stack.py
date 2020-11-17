# python3

import sys


class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MinStack:
    def __init__(self):
        self.head = None
        self.minimum = -float("inf")

    def __repr__(self):
        node = self.head
        stack = ""

        if node is None:
            return stack

        while node:
            stack = str(node.val) + " " + stack
            node = node.next
        
        return stack

    def add(self, val):
        if self.head is None:
            self.minimum = val

        else:
            if val < self.minimum:
                old_min = self.minimum
                self.minimum = val
                val = 2 * val - old_min
        
        node = LinkedListNode(val)
        node.next = self.head
        self.head = node


    def pop(self):
        if self.head is None:
            return "empty stack"
        
        else:
            top = self.head.val
            if top < self.minimum:
                temp = top
                top = self.minimum
                self.minimum = 2 * self.minimum - temp
            
            node = self.head
            self.head = self.head.next
            node.next = None
        
        return top

    def minimum_val(self):
        return self.minimum


def main():
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip().split()
        
    stack = MinStack()
    for line in lines:
        if line[0] == 'add':
            stack.add(int(line[1]))
            print(stack)
        
        if line[0] == 'pop':
            val = stack.pop()
            print(val)
        
        if line[0] == "min": 
            print(stack.minimum_val())


if __name__ == '__main__':
    main()
        
# python3

import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 1 if head is not None else 0

    def __repr__(self):
        if self.head is None:
            return ''
        node = self.head
        linkedlist = str(node.value)
        while node.next:
            node = node.next
            linkedlist += '->' + str(node.value)

        return linkedlist

    def return_array(self):
        if self.head is None:
            return []
        array = []
        node = self.head
        array.append(node.value)
        while node.next:
            node = node.next
            array.append(node.value)

        return array

    def __len__(self):
        return self.length

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def remove(self, n):
        """ remove method deletes elements based on their
            indexes or position in the linked list """
        if self.head is None or (n < 0 or self.length <= n):
            return "nothing to remove"
        else:
            self.length -= 1

        count = 0
        node = self.head
        prev = None

        while count < n:
            prev = node
            node = node.next
            count += 1

        # this indicates that query was the head value
        if prev is None:
            prev = node.next
            node.next = None
            self.head = prev

        else:
            prev.next = node.next
            node.next = None

    def search(self, query):
        if self.head is None:
            return "failure"

        node = self.head

        while node.next:
            if node.value == query:
                return "success"
            node = node.next

        if node.value == query:
            return "success"

        return "failure"

    def search_nth(self, n):
        if n < 0 or n >= self.length - 1 or self.head is None:
            return "doesn't exist"

        count = 0
        node = self.head

        while count < n:
            node = node.next
            count += 1

        return node.value

    def middle(self):
        if self.head is None:
            return "empty linked list"

        fast = self.head
        slow = self.head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow.value

    def reverse(self):
        if self.head is None:
            return "empty linked list"

        node = self.head
        prev = None

        while node.next:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        node.next = prev

        self.head = node


def main():

    data = sys.stdin.readline()
    data = list(map(int, data.split()))
    linkedlist = LinkedList()
    for val in data:
        linkedlist.add(val)

    print(linkedlist)
    print(linkedlist.return_array())

    linkedlist.reverse()

    print(linkedlist)
    print(linkedlist.return_array())
    print("The length of the linked list is: ", len(linkedlist))

    value = int(input("pick a number to search: "))

    print(linkedlist.search(value))
    print("the middle of the linked list is: ", linkedlist.middle())

    val = linkedlist.middle()

    print(linkedlist)

    val = linkedlist.middle()

    print(linkedlist)
    print("pop")
    linkedlist.remove(0)

    print(linkedlist)
    print("pop")

    linkedlist.remove(0)

    print(linkedlist)
    print("the first element is:", linkedlist.search_nth(0))

    linkedlist.reverse()

    print(linkedlist)
    print("the 12-th element is:", linkedlist.search_nth(11))


if __name__ == '__main__':
    main()

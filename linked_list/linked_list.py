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
        node = self.head
        linkedlist = str(node.value)
        while node.next:
            node = node.next
            linkedlist += '->' + str(node.value)

        return linkedlist
    
    def __len__(self):
        return self.length

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def search(self, query):
        node = self.head
        
        while node.next:
            node = node.next
            if node.value == query:
                return "success"

        return "failure"

    def middle(self):
        fast = self.head
        slow = self.head
        while fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow.value

    def reverse(self):
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
    linkedlist.reverse()
    print(linkedlist)
    print("The length of the linked list is: ", len(linkedlist))
    value = int(input("pick a number to search: "))
    print(linkedlist.search(value))
    print("the middle of the linked list is: ",linkedlist.middle())
    linkedlist.reverse()
    print(linkedlist)


if __name__ == '__main__':
    main()
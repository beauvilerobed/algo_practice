import sys
import random


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.value)


class BST:
    def __init__(self, root=None):
        self.root = root
        self.all_nodes = ""

    def __repr__(self):

        def inorder_traversal(node):
            if node is None:
                return

            inorder_traversal(node.left)
            self.all_nodes += " " + str(node.value)
            inorder_traversal(node.right)
            
        self.all_nodes = ''
        inorder_traversal(self.root)
        return self.all_nodes

    def insert(self, value):

        node = Node(value)

        if self.root == None:
            self.root = node
        
        else:
            found_node = self.insert_util(value)
            if found_node.value > value:
                found_node.left = node
                node.parent = found_node
            else:
                found_node.right = node
                node.parent = found_node
    
    def delete(self, value):
        if self.root == None:
            return None

        found_node = self.insert_util(value, find=True)
        next_node = self.next(found_node)
        parent = next_node.parent

        self.swap(found_node, next_node, parent)


    def swap(self, found_node, next_node, parent):
        if parent == found_node:
            found_node.value = next_node.value
            if found_node.right:
                found_node.right = next_node.right
            elif found_node.left:
                found_node.left = next_node.left

        else:
            found_node.value = next_node.value
            if found_node.right:
                parent.left = next_node.right
            elif found_node.right:
                parent.right = next_node.left
            else:
                parent = found_node.parent
                if parent.left:
                    parent.left = None
                else:
                    parent.right = None


    def insert_util(self, value, find=False):
        
        node = self.root

        while node.left or node.right:
            if value < node.value:
                if node.left is None:
                    return node
                else:   
                    node = node.left

            if value >= node.value:
                if find and node.value == value:
                    return node

                if node.right is None:
                    return node
                else:
                    node = node.right             

        return node

    def next(self, node):
        if node is None:
            return None

        if node.right:
            node = node.right
            while node.left:
                node = node.left

        
        elif node.left:
            node = node.left
            while node.right:
                node = node.right


        return node



def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    bst = BST()
    length = len(nums) - 1
    random_index = random.randint(0, length)
    for num in nums:
        bst.insert(num)

    print(bst)
    val = nums[random_index]
    print(val)
    bst.delete(val)
    print(bst)


if __name__ == '__main__':
    main()

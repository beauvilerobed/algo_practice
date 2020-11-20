import sys

class Node:
    def __init__(self, value):
        self.value = value
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
            found_node = self.helper_method(self.root, value)
            if found_node.value > value:
                found_node.left = node
            
            else:
                found_node.right = node
    
    def helper_method(self, node, value):
        while node.left or node.right:
            if value < node.value:
                if node.left is None:
                    return node
                else:   
                    node = node.left

            if value >= node.value:
                if node.right is None:
                    return node
                else:
                    node = node.right             

        return node

        
    # def delete(self, value):

def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    bst = BST()
    for num in nums:
        bst.insert(num)

    print(bst)


if __name__ == '__main__':
    main()

import sys
from collections import Counter


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)


def print_tree(root):
    if root == None:
        return 

    print(root, end=" ")
    print_tree(root.left)
    print_tree(root.right)


def isSumTree(node): 
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return node.data

    if node.data == isSumTree(node.left) + isSumTree(node.right):
        return 2 * node.data
    
    return float("inf")



def main():
    root = TreeNode(26)
    root.left = TreeNode(10)
    root.right = TreeNode(3)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)

    if isSumTree(root) != float("inf"):
        print("This is a SumTree")
    else:
        print("This is not a SumTree")

    print_tree(root)


if __name__ == '__main__':
    main()

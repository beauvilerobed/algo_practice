import sys


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

def isSumTree(root):
    
    node = root

    if node.left is None and node.right is None:
        return True

    if node.key == isSumTree(node.left) + isSumTree(node.right):
        return 
# Helper functions because of issues with recursion in class methods
def printTreeHelper(node):
    # base case: 
    #   - implicit -> if this node is None, nothing to do
    #   - meaning -> if this node is None then the caller was pointing to none on this subtree
    if node:
        print(node.data)

        # explore left and right subtrees
        printTreeHelper(node.left)
        printTreeHelper(node.right)

def invertTreeHelper(node):
    # base case: 
    #   - implicit -> if this node is None, nothing to do
    #   - meaning -> if this node is None then the caller was pointing to none on this subtree
    if node:
        # choose
        left = node.left
        right = node.right

        # explore both options of the tree
        invertTreeHelper(left)
        invertTreeHelper(right)

        # unchoose -> swap the nodes
        node.left = right
        node.right = left
# ----------------------------------------------------------------------------------------------------




# engine of the binary tree -> node value points at left and right nodes (initially none)
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# ----------------------------------------------------------------------------------------------------

 
# binary tree class which contains printing and inversion methods
class BinaryTree:
    def __init__(self, head=None):
        self.head = head

    def printTree(self):
        printTreeHelper(self.head)

    def invertTree(self):
        invertTreeHelper(self.head)
# ----------------------------------------------------------------------------------------------------




# Test case to make sure implementation of the binary tree goes as expected
# Define all the nodes of the tree
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)

# Structure the tree
bt = BinaryTree(first)
bt.head.left = second
second.left = fourth
second.right = fifth
bt.head.right = third
third.left = sixth
third.right = seventh 
#             1
#           /  \
#          2    3
#        / \   / \
#       4  5  6  7
bt.printTree()
print('----')

# Invert the tree
bt.invertTree()
#             1
#           /  \
#          3    2
#        / \   / \
#       7  6  5  4
bt.printTree()

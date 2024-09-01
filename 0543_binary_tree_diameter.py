from typing import Optional
from utils.tree_utils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Analysis:
# diameter passing through a node = note's left height + right height
# diameter of a tree = max(diameter of every node)
# height = 0 if it's leaf else height = max (height left sub, height right sub) + 1

class Solution:
    def find_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        if node.left is None and node.right is None:
            return 0

        if hasattr(node, 'height'):
            return node.height

        node.height = max(self.find_height(node.left), self.find_height(node.right)) + 1
        return node.height

    def find_diameter_passing_node(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        diameter_passing_node = self.find_height(node.left) + self.find_height(node.right)
        if node.left:
            diameter_passing_node += 1
        if node.right:
            diameter_passing_node += 1

        return diameter_passing_node

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        return max(
            self.find_diameter_passing_node(root),
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )





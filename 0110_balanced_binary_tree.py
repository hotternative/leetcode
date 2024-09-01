# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional
from utils.tree_utils import TreeNode

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(node: Optional[TreeNode]):
            if not node:
                return 0
            if hasattr(node, 'h'):
                return node.h

            if node.left is None and node.right is None:
                node.h = 1
                return 1

            else:
                return max(height(node.left), height(node.right)) + 1

        nodes = [root]
        while nodes:
            n = nodes.pop()
            if abs(height(n.left) - height(n.right)) > 1:
                return False
            else:
                if n.left:
                    nodes.append(n.left)
                if n.right:
                    nodes.append(n.right)

        return True

class Solution2:
    # recursion April 2024
    def calculate_height_of_node(self, node):
        if node:
            left_height = self.calculate_height_of_node(node.left)
            right_height = self.calculate_height_of_node(node.right)
            node.height = max(left_height, right_height) + 1
            return node.height
        else:
            return 0


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.calculate_height_of_node(root)
        left_height = root.left.height if root.left else 0
        right_height = root.right.height if root.right else 0

        height_diff = abs(left_height - right_height)
        if self.isBalanced(root.left) and self.isBalanced(root.right) and height_diff <= 1:
            return True
        else:
            return False


class Solution3:
    # improved recursion April 2024
    # calculate height in the same recursion

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            left_height = root.left.height if root.left else 0
            right_height = root.right.height if root.right else 0
            root.height = max(left_height, right_height) + 1
            if abs(left_height - right_height) <= 1:
                return True
        else:
            return False
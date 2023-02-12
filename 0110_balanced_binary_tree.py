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


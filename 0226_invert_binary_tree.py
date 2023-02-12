# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from utils.tree_utils import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Runtime 31 ms Beats 78.60%; Memory 13.8 MB Beats 95.1%"""
        nodes_to_invert = []
        if root:
            nodes_to_invert.append(root)
        else:
            return None

        while nodes_to_invert:
            n = nodes_to_invert.pop()
            n.right, n.left = n.left, n.right
            if n.left:
                nodes_to_invert.append(n.left)
            if n.right:
                nodes_to_invert.append(n.right)
        return root




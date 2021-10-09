"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge the two trees into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up as the
new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""
from typing import Optional
from utils.tree_utils import TreeNode
# Definition for a binary tree node.

class Solution:
    """
    Runtime: 88 ms, faster than 64.04% of Python3 online submissions.
    Memory Usage: 15.1 MB, less than 98.72% of Python3 online submissions.
    """
    def mergeTrees(
            self,
            root1: Optional[TreeNode],
            root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        root2.val += root1.val
        root2.left = self.mergeTrees(root1.left, root2.left)
        root2.right = self.mergeTrees(root1.right, root2.right)
        return root2
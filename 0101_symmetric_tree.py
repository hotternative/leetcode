from typing import Optional
from utils.tree_utils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        cln = current_level_nodes = [root]

        while any(cln):

            nln = []  # next level nodes
            clv = []  # current level values

            for n in cln:
                clv.append(n.val if n else None)
                nln.append(n.left if n else None)
                nln.append(n.right if n else None)

            if clv != clv[::-1]:
                return False
            else:
                cln = nln

        return True


class Solution2:
    # BFS， but serialise the tree first
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # serialise the tree
        cln = [root]
        serialised_tree = []
        while any(cln):
            nln = []
            for n in cln:
                serialised_tree.append(n.val if n else None)
                nln.append(n.left if n else None)
                nln.append(n.right if n else None)
            cln = nln
        n = 1

        while 2 ** n - 1 <= len(serialised_tree):
            slice = serialised_tree[2 ** (n - 1) - 1:2 ** n - 1]

            if slice != slice[::-1]:
                return False
            n += 1
        return True


class Solution3:
    # recursive
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (left.val == right.val) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)



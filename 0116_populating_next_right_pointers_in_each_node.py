"""
You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children.

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

"""
from utils.tree_utils import TreeNode
from collections import deque

class Solution:
    def connect1(self, root: TreeNode) -> TreeNode:
        """
        Iterative BFS
        Runtime: 64 ms, faster than 68.30% of Python3 online submissions
        Memory Usage: 15.7 MB, less than 31.58% of Python3 online submissions

        Denote tree height H and total number of nodes M.
        -> Number of leaf nodes 2**(H-1)
        Time complexity: we loop through each node once O(M)
        Space comlexity: at the leaf level we use most memory O(2**(H-1))
        """
        cur_iteration = []
        next_iteration = [root]
        while next_iteration:
            cur_iteration, next_iteration = next_iteration, []
            for i, node in enumerate(cur_iteration):
                node.next = cur_iteration[i+1] if i < len(cur_iteration)-1 else None
                if node.left:
                    next_iteration.append(node.left)
                if node.right:
                    next_iteration.append(node.right)
        return root

    def connect(self, root: TreeNode) -> TreeNode:
        """
        Follow up:
        You may only use constant extra space.
        You may assume implicit stack space does not count as extra space for this problem.

        Solution: recursion

        Runtime: 252 ms, faster than 5.12% of Python3 online submissions.
        Memory Usage: 15.6 MB, less than 71.07% of Python3 online submissions.
        """
        if not root:
            return root
        root.next = None

        def connect_nodes(node1, node2):
            if node1 == None:
                return
            node1.next = node2
            connect_nodes(node1.left, node1.right)
            connect_nodes(node1.right, node2.left)
            connect_nodes(node2.left, node2.right)

        connect_nodes(root.left, root.right)
        return root
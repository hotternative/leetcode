from utils.tree_utils import TreeNode
from typing import Optional

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Runtime 38 ms Beats 29.8% Memory 13.7 MB Beats 94.81%
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def root_to_list(root: TreeNode):
    cln = [root]
    serialised_tree = []
    while any(cln):
        nln = []
        for n in cln:
            serialised_tree.append(n.val if n else None)
            nln.append(n.left if n else None)
            nln.append(n.right if n else None)
        cln = nln
    return serialised_tree
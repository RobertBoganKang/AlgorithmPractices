"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        pre = 0
        i = 0
        result = True

        def dfs(node):
            nonlocal i, pre, result
            if not result:
                if node != None:
                    return
                dfs(node.left)
                if i != 0 and pre >= node.val:
                    result = False
                i += 1
                pre = node.val
                dfs(node.right)

        dfs(root)
        return result

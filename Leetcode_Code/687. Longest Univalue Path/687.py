class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        max_case = 0

        def dfs(node):
            nonlocal max_case
            if not node.left and not node.right:
                return 0
            lv = rv = 0
            if node.left:
                if node.val == node.left.val:
                    lv = dfs(node.left) + 1
                else:
                    dfs(node.left)
            if node.right:
                if node.val == node.right.val:
                    rv = dfs(node.right) + 1
                else:
                    dfs(node.right)
            max_case = max(max_case, lv + rv)
            # only one longer path could be kept to calculate the further parent loops,
            # not the current loop
            return max(lv, rv)

        dfs(root)
        return max_case

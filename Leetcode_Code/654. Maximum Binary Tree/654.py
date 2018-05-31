class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def partition(start, end):
            max_num = nums[start]
            max_pos = start
            for i in range(start, end):
                if max_num < nums[i]:
                    max_pos = i
                    max_num = nums[i]
            return max_pos, max_num

        def dfs(start, end):
            if start >= end:
                return None
            else:
                max_pos, max_num = partition(start, end)
                node = TreeNode(max_num)
                node.left = dfs(start, max_pos)
                node.right = dfs(max_pos + 1, end)
                return node

        return dfs(0, len(nums))

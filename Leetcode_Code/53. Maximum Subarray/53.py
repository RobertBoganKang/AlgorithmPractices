class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = curmin = curmax = nums[0]
        for i in range(1, len(nums)):
            print(max_num)
            cur = nums[i]
            curmax, curmin = max(curmax * cur, curmin * cur, cur), min(curmax * cur, curmin * cur, cur)
            max_num = max(curmax, max_num)
        return max_num


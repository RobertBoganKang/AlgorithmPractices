class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set()
        for i in range(len(nums)):
            num_set.add(nums[i])
        result = []
        for i in range(1, len(nums) + 1):
            if i not in num_set:
                result.append(i)
        return result

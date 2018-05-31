class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        # build hashmap
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        # find the single element
        for i in hashmap:
            if hashmap[i] == 1:
                return i
        return None

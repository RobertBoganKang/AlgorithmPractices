class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        # build hashmap
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        # find the single element
        result = []
        for i in hashmap:
            if hashmap[i] == 2:
                result.append(i)
        return result

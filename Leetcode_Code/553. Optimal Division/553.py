class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums is None:
            return ""
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        string_builder = ""
        string_builder += str(nums[0])
        string_builder += "/("
        i = 1
        while i < len(nums):
            string_builder += str(nums[i])
            if i != len(nums) - 1:
                string_builder += "/"
            i += 1
        string_builder += ")"
        return string_builder


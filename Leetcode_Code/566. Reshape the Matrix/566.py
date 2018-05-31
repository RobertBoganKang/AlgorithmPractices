class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # assume that the 2D array is a matrix
        if nums is None or len(nums) == 0:
            return []
        d1 = len(nums)
        d2 = len(nums[0])
        if d1 * d2 != r * c:
            return nums
        else:
            result = []
            temp = []
            for i in range(d1 * d2):
                temp.append(nums[i // d2][i % d2])
                if i % c == c - 1:
                    result.append(temp)
                    temp = []
            return result

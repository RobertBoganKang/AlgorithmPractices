class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None

        def partition(start, end):
            nonlocal result
            if result is None:
                if end - start <= 2:
                    result = nums[start]
                else:
                    partition_point = round((end - start + 1) / 4) * 2 + start
                    if nums[partition_point - 1] == nums[partition_point - 2]:
                        partition(partition_point, end)
                    else:
                        partition(start, partition_point)

        partition(0, len(nums))
        return result


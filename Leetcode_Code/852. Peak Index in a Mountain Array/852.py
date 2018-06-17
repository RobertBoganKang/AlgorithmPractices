class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start = 1
        while start < len(A) - 1:
            if A[start] >= A[start + 1]:
                break
            start += 1

        end = len(A) - 1
        while end > 1:
            if A[end] >= A[end - 1]:
                break
            end -= 1
        if start == end:
            return start
        return -1

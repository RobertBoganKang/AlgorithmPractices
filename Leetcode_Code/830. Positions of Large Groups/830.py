class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if S is None or len(S) < 2:
            return []
        S += "#"
        start = 0
        i = 1
        result = []
        while i < len(S):
            if S[i] != S[start]:
                if i > start + 2:
                    result.append([start, i - 1])
                start = i
            i += 1
        return result

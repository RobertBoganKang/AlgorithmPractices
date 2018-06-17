class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        if S is None or C is None or S == "":
            return []
        #
        result = [0 for _ in range(len(S))]
        # detect first letter
        i = 0
        last = 0
        count = 0
        # loop second or more
        while i < len(S):
            num = 1
            while i < len(S) and S[i] != C:
                result[i] = num
                num += 1
                i += 1
            if i >= len(S):
                if count == 0:
                    return [0 for _ in range(len(S))]
                break

            if count == 0:
                back_num = 0
            else:
                back_num = num // 2
            # backtrace
            j = i
            num = 0
            while j >= last + back_num:
                result[j] = num
                num += 1
                j -= 1
            count += 1
            i += 1
            last = i
        return result


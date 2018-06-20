class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        if len(strs) < 2:
            return strs[0]
        common = ""
        test = True
        j = 0
        while test:
            char = ""
            for i in range(len(strs)):
                if j < len(strs[i]):
                    if i == 0:
                        char = strs[0][j]
                    elif char != strs[i][j]:
                        char = ""
                        test = False
                        break
                else:
                    char = ""
                    test = False
            common += char
            j += 1
        return common

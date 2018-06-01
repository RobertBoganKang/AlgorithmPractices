class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        length = len(S)
        string_builder = []
        i = length - 1
        # index of the valid letters
        valid = 0
        while i >= 0:
            c = S[i]
            if c != '-':
                if valid != 0 and valid % K == 0:
                    string_builder.append("-")
                if 'a' <= c <= 'z':
                    string_builder.append(c.upper())
                else:
                    string_builder.append(c)
                valid += 1
            i -= 1
        string_builder.reverse()
        return ''.join(string_builder)

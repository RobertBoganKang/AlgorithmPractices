class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :param S: String
        :param K: Integer
        :return: String
        """

        length = len(S)
        string_builder = []
        i = length - 1
        # index of the valid letters
        valid = 0
        while i >= 0:
            c = S[i]
            if '0' <= c <= '9' or 'A' <= c <= 'Z' or 'a' <= c <= 'z':
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

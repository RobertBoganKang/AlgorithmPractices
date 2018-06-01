class Solution:
    def license_key_formatting(self, string, group):
        """
        :param string: String
        :param group: Integer
        :return: String
        """
        
        length = len(string)
        string_builder = []
        i = length - 1
        # index of the valid letters
        valid = 0
        while i >= 0:
            c = string[i]
            if '0' <= c <= '9' or 'A' <= c <= 'Z' or 'a' <= c <= 'z':
                if valid != 0 and valid % group == 0:
                    string_builder.append("-")
                if 'a' <= c <= 'z':
                    string_builder.append(c.upper())
                else:
                    string_builder.append(c)
                valid += 1
            i -= 1
        string_builder.reverse()
        return ''.join(string_builder)


s = Solution()
print(s.license_key_formatting("5F3Z-2e-9-w", 4))
print(s.license_key_formatting("2-5g-3-J", 2))

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def build_string(str):
            char_arr = []
            for i in range(len(str)):
                c = str[i]
                if c == '#':
                    if len(char_arr) != 0:
                        char_arr.pop()
                    else:
                        continue
                else:
                    char_arr.append(c)
            return char_arr

        return build_string(S) == build_string(T)


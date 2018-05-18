class Solution:
    """
    @param str: a string
    @return: a compressed string
    """

    def decompress(self, str):
        stringbuilder = ''
        pre = ''
        i = 0
        while i < len(str):
            c = str[i]
            if 'a' <= c <= 'z':
                pre = c
                stringbuilder += c
                i += 1
            else:
                num = 0
                while i < len(str) and '0' <= str[i] <= '9':
                    num = num * 10 + int(str[i])
                    i += 1
                for _ in range(num - 1):
                    stringbuilder += pre
        return stringbuilder

    def compress(self, strs):
        string = strs
        string += '#'
        stringbuilder = ''
        pre = ''
        i = 0
        count = 0
        while i < len(string):
            c = string[i]
            if c == pre:
                count += 1
                i += 1
                continue
            else:
                stringbuilder += pre
                if i != 0:
                    stringbuilder += str(count + 1)
                count = 0
            pre = c
            i += 1
        if len(stringbuilder) >= len(strs):
            return strs
        else:
            return stringbuilder


def main():
    s = Solution()
    print(s.compress('abcccc'))
    print(s.decompress('a2b1c5a3'))


if __name__ == '__main__':
    main()

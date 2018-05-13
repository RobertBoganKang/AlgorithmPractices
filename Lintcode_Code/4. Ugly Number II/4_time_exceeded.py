class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        def isUgly(num):
            while num > 1:
                if num % 2 == 0:
                    num = num // 2
                elif num % 3 == 0:
                    num = num // 3
                elif num % 5 == 0:
                    num = num // 5
                else:
                    return False
            return True

        i = 0
        while n > 0:
            i += 1
            if isUgly(i):
                n -= 1
        return i


def main():
    s = Solution()
    print(s.nthUglyNumber(599))


if __name__ == '__main__':
    main()

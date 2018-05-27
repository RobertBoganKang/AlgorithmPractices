class Solution:
    def square_sum(self, num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num = num // 10
        return total

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sets = set()
        while n not in sets and n != 1:
            sets.add(n)
            n = self.square_sum(n)
        return n == 1

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def dfs(dx, dn):
            if dn == 0:
                return 1
            if dn < 0:
                return 1 / dfs(dx, -dn)
            if dn % 2 == 1:
                return dx * dfs(dx * dx, dn // 2)
            else:
                return dfs(dx * dx, dn // 2)

        return dfs(x, n)

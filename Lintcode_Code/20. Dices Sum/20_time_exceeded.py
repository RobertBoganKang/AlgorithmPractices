class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        mp = {}
        whole = 0

        def dfs(level, total):
            nonlocal mp, whole
            if level == 0:
                if total in mp:
                    mp[total] += 1
                else:
                    mp[total] = 1
                whole += 1
                return
            for i in range(1, 7):
                dfs(level - 1, total + i)

        dfs(n, 0)
        arr = []
        for c in mp:
            arr.append([c, mp[c] / whole])
        return arr

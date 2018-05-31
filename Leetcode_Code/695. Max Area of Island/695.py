class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return None
        d1 = len(grid)
        d2 = len(grid[0])

        def dfs(_i, _j):
            if _i < 0 or _j < 0 or _i >= d1 or _j >= d2 or grid[_i][_j] == 0:
                return 0
            else:
                grid[_i][_j] = 0
                return 1 + dfs(_i + 1, _j) + dfs(_i, _j + 1) + dfs(_i - 1, _j) + dfs(_i, _j - 1)

        max_island = 0
        for i in range(d1):
            for j in range(d2):
                if grid[i][j] == 1:
                    max_island = max(max_island, dfs(i, j))
        return max_island

class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def check_magic_matrix(idx, idy):
            # first row sum as target
            target = grid[idx][idy] + grid[idx][idy + 1] + grid[idx][idy + 2]
            # check rows
            for i in range(1, 3):
                total = 0
                for j in range(3):
                    total += grid[idx + i][idy + j]
                if total != target:
                    return False

            distinct = set()
            # check columns
            for j in range(3):
                total = 0
                for i in range(3):
                    if grid[idx + j][idy + i] > 9 or grid[idx + j][idy + i] < 1:
                        return False
                    if grid[idx + j][idy + i] in distinct:
                        return False
                    else:
                        distinct.add(grid[idx + j][idy + i])
                    total += grid[idx + j][idy + i]
                if total != target:
                    return False
            # check diagonals
            if grid[idx][idy] + grid[idx + 1][idy + 1] + grid[idx + 2][idy + 2] != target \
                    or grid[idx][idy + 2] + grid[idx + 1][idy + 1] + grid[idx + 2][idy] != target:
                return False
            return True

        result = 0
        for I in range(len(grid) - 2):
            for J in range(len(grid[0]) - 2):
                if check_magic_matrix(I, J):
                    result += 1
        return result

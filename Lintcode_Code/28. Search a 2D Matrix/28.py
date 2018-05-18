class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        d1 = len(matrix)

        if d1 == 0:
            return False
        d2 = len(matrix[0])
        result = False

        def cvt(i):
            nonlocal d1, d2
            return i // d2, i % d2

        def partition(small, mid, large):
            nonlocal result
            if not result:
                # convert space
                sidx = cvt(small)
                midx = cvt(mid)
                lidx = cvt(large)
                snum = matrix[sidx[0]][sidx[1]]
                mnum = matrix[midx[0]][midx[1]]
                lnum = matrix[lidx[0]][lidx[1]]

                if snum == target or mnum == target or lnum == target:
                    result = True
                elif small == mid or large == mid:
                    return
                elif target > mnum:
                    partition(mid, (mid + large) // 2, large)
                elif target < mnum:
                    partition(small, (mid + small) // 2, mid)

        partition(0, (d1 * d2 - 1) // 2, d1 * d2 - 1)
        return result


def main():
    s = Solution()
    matrix = [

    ]
    print(s.searchMatrix(matrix, 1))


if __name__ == '__main__':
    main()

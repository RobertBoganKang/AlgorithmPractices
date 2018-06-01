class Solution:
    def spiral_matrix(self, matrix):
        """
        :param matrix: List(List())
        :return: List()
        """
        result = []
        if matrix is None or len(matrix) == 0:
            return result
        # define a True/False table
        tf_table = [[False for _ in range(len(matrix[0]) + 2)] for _ in range(len(matrix) + 2)]
        for i in range(len(matrix) + 2):
            tf_table[i][0] = True
            tf_table[i][-1] = True
        for i in range(len(matrix[0]) + 2):
            tf_table[0][i] = True
            tf_table[-1][i] = True
        # direction {right: 1, down: 2, left: 3, up: 4}
        direction = 0
        # coordinate
        i = j = 1
        while not (tf_table[j + 1][i] and tf_table[j][i + 1] and tf_table[j - 1][i] and tf_table[j][i - 1]):
            # turning
            if direction == 0 and tf_table[j][i + 1]:
                direction = 1
            if direction == 1 and tf_table[j + 1][i]:
                direction = 2
            if direction == 2 and tf_table[j][i - 1]:
                direction = 3
            if direction == 3 and tf_table[j - 1][i]:
                direction = 0
            # print(str(i - 1) + " : " + str(j - 1) + " @ " + str(direction))
            result.append(matrix[j - 1][i - 1])

            # tag the state now
            tf_table[j][i] = True

            # running
            if direction == 0:
                i += 1
            elif direction == 1:
                j += 1
            elif direction == 2:
                i -= 1
            elif direction == 3:
                j -= 1
        # add last element
        result.append(matrix[j - 1][i - 1])
        return result


s = Solution()
print(s.spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

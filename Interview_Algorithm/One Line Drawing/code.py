class Solution:
    def __init__(self):
        self.initial_pos = [0, 0]
        self.height = 0
        self.width = 0

    def one_line_draw(self, matrix):
        """
        solve one-line drawing
        :param matrix: list(list(int))
        1 is pathway, 0 is not a pathway, -1 is the initial position
        example:
        [[1,1,1,1,1,1],
        [-1,0,1,1,1,1],
        [0,1,1,1,1,0],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,0,1]]
        :return: list(list(str));
        the solution of {up, down, left, right}
        """
        # get the dimension of matrix
        self.height = len(matrix)
        self.width = len(matrix[0])

        # count the number of pathways
        total = 1
        # initial potition
        initpos = [0, 0]
        for i in range(self.height):
            for j in range(self.width):
                total += matrix[i][j]
                if matrix[i][j] == -1:
                    initpos = [i, j]
        self.initial_pos = initpos

        # solution stack
        stk = []
        result = []

        def dfs(pos):
            nonlocal total, stk, result, matrix
            # print(stk, total)
            if total == 0:
                result.append(stk.copy())
                return
            # left
            if pos[1] > 0 and matrix[pos[0]][pos[1] - 1] > 0:
                total -= 1
                stk.append("<")
                matrix[pos[0]][pos[1] - 1] = 0
                dfs([pos[0], pos[1] - 1])
                matrix[pos[0]][pos[1] - 1] = 1
                stk.pop()
                total += 1
            # right
            if pos[1] < self.width - 1 and matrix[pos[0]][pos[1] + 1] > 0:
                total -= 1
                stk.append(">")
                matrix[pos[0]][pos[1] + 1] = 0
                dfs([pos[0], pos[1] + 1])
                matrix[pos[0]][pos[1] + 1] = 1
                stk.pop()
                total += 1
            # up
            if pos[0] > 0 and matrix[pos[0] - 1][pos[1]] > 0:
                total -= 1
                stk.append("^")
                matrix[pos[0] - 1][pos[1]] = 0
                dfs([pos[0] - 1, pos[1]])
                matrix[pos[0] - 1][pos[1]] = 1
                stk.pop()
                total += 1
            # down
            if pos[0] < self.height - 1 and matrix[pos[0] + 1][pos[1]] > 0:
                total -= 1
                stk.append("v")
                matrix[pos[0] + 1][pos[1]] = 0
                dfs([pos[0] + 1, pos[1]])
                matrix[pos[0] + 1][pos[1]] = 1
                stk.pop()
                total += 1

        dfs(initpos)
        return result

    def blank_matrix(self):
        return [['_' for _ in range(self.width)] for _ in range(self.height)]

    def print_drawing(self, sols):
        """
        print the solution drawings
        :param sols: list(list(str))
        :return: null, just print the result
        """
        count = 0
        for sol in sols:
            count += 1
            matrix = self.blank_matrix().copy()
            pos = self.initial_pos.copy()
            counter = 0
            matrix[pos[0]][pos[1]] = "@"
            for i in range(len(sol)):
                counter += 1
                if sol[i] == '<':
                    pos[1] -= 1
                if sol[i] == '>':
                    pos[1] += 1
                if sol[i] == '^':
                    pos[0] -= 1
                if sol[i] == 'v':
                    pos[0] += 1
                matrix[pos[0]][pos[1]] = str(counter)
            # print it
            print("Sotution {0}:".format(count))
            for i in range(len(matrix)):
                print("\t".join(matrix[i]))


def main():
    s = Solution()
    case = [[1, 1, 1, 1, 1, 1],
            [-1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1]]
    r = s.one_line_draw(case)
    s.print_drawing(r)


if __name__ == '__main__':
    main()

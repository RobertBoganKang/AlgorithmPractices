import heapq


class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """

    def kthSmallest(self, matrix, k):
        queue = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(queue, -matrix[i][j])
                if len(queue) > k:
                    heapq.heappop(queue)
        return -queue[0]

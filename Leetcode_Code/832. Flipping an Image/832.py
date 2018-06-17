class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        def reflect_inverse(arr):
            if len(arr) % 2 == 1:
                arr[len(arr) // 2] = 1 - arr[len(arr) // 2]
            for i in range(len(arr) // 2):
                arr[i], arr[len(arr) - i - 1] = 1 - arr[len(arr) - i - 1], 1 - arr[i]

        for j in range(len(A)):
            reflect_inverse(A[j])
        return A

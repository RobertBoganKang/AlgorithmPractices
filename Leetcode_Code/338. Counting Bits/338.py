import math


class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        num += 1
        if num <= 2:
            return [0, 1][0:num]
        arr = [0 for _ in range(num)]
        arr[0] = 0
        arr[1] = 1

        def index(idx):
            return idx % (2 ** int(math.log2(idx)))

        for i in range(2, num):
            arr[i] = 1 + arr[index(i)]
        return arr

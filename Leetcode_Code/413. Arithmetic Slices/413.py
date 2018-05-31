class Solution:
    def numberOfArithmeticSlices(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        if a is None or len(a) < 3:
            return 0
        # calculate differences array
        diff_arr = []
        for i in range(len(a) - 1):
            diff_arr.append(a[i + 1] - a[i])
        # calculate sub-sequences slice
        diff_arr.append(diff_arr[-1] + 1)
        count = 1
        count_arr = []
        for i in range(len(diff_arr) - 1):
            if diff_arr[i + 1] != diff_arr[i]:
                if count >= 2:
                    count_arr.append(count)
                count = 1
            else:
                count += 1
        # count the result
        total = 0
        for i in range(len(count_arr)):
            n = count_arr[i] - 1
            total += (n + 1) * n // 2
        return total

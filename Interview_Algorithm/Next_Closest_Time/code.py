class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h2 = int(time[0])
        h1 = int(time[1])
        m2 = int(time[3])
        m1 = int(time[4])
        digit_arr = [h2, h1, m2, m1]
        digit_arr = list(set(digit_arr))
        digit_arr.sort()

        def next_max(digit):
            i = 0
            while i < len(digit_arr) and digit_arr[i] <= digit:
                i += 1
            if i == len(digit_arr):
                i -= 1
            return digit_arr[i]

        # first digit
        if m1 < digit_arr[-1]:
            return time[0:4] + str(next_max(m1))
        # second digit
        nm2 = next_max(m2)
        if nm2 < 6 and nm2 < digit_arr[-1]:
            return time[0:3] + str(nm2) + str(digit_arr[0])
        # third digit
        if h2 < 2:
            nh1 = next_max(h1)
            if h1 < digit_arr[-1]:
                return str(time[0]) + str(nh1) + ":" + str(digit_arr[0]) + str(digit_arr[0])
            nh2 = next_max(h2)
            if nh2 < 3:
                return str(nh2) + str(digit_arr[0]) + ":" + str(digit_arr[0]) + str(digit_arr[0])
        else:
            nh1 = next_max(h1)
            if nh1 <= 3:
                return str(h2) + str(nh1) + ":" + str(digit_arr[0]) + str(digit_arr[0])
            else:
                return str(digit_arr[0]) + str(digit_arr[0]) + ":" + str(digit_arr[0]) + str(digit_arr[0])


s = Solution()
print(s.nextClosestTime("13:55"))

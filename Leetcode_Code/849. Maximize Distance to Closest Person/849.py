class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        if seats is None or len(seats) == 0:
            return 0
        max_seat = 0
        # start case
        start = 0
        while seats[start] != 1:
            start += 1
        max_seat = start

        # end case
        end = len(seats) - 1
        while seats[end] != 1:
            end -= 1
        max_seat = max(max_seat, len(seats) - end - 1)

        # middle
        idx = start
        last = start
        while idx <= end:
            if seats[idx] == 1:
                max_seat = max(max_seat, (idx - last) // 2)
                last = idx
            idx += 1
        return max_seat


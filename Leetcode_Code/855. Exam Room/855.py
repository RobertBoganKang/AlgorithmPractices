class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.exam_room = []
        self.exam_room_size = N

    def seat(self):
        """
        :rtype: int
        """
        if len(self.exam_room) == 0:
            self.exam_room.append(0)
            return 0
        elif len(self.exam_room) == 1:
            pos = self.exam_room[0]
            if pos > self.exam_room_size - pos - 1:
                self.insert_sorted(self.exam_room, 0)
                return 0
            else:
                self.insert_sorted(self.exam_room, self.exam_room_size - 1)
                return self.exam_room_size - 1
        else:
            i = 0
            gap = 0
            pos = -1
            if self.exam_room[0] > 0:
                gap = self.exam_room[0]
                pos = 0
            while i < len(self.exam_room) - 1:
                cur_gap = (self.exam_room[i + 1] - self.exam_room[i]) // 2
                if cur_gap == 0:
                    i += 1
                    continue
                elif cur_gap > gap:
                    gap = cur_gap
                    pos = self.exam_room[i] + cur_gap
                i += 1
            if self.exam_room[-1] < self.exam_room_size - 1:
                cur_gap = self.exam_room_size - 1 - self.exam_room[-1]
                if cur_gap > gap:
                    gap = cur_gap
                    pos = self.exam_room_size - 1
            if pos == -1:
                return None
            self.insert_sorted(self.exam_room, pos)
            return pos

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        if p in self.exam_room:
            self.exam_room.remove(p)

    def insert_sorted(self, arr, num):
        """
        insert element as sorted array
        :param arr: List(int)
        :param num: int
        :return:
        """
        i = 0
        while i < len(arr) and arr[i] < num:
            i += 1
        arr.insert(i, num)
        return arr


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

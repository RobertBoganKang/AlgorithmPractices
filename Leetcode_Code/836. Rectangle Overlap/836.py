class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        h1 = [rec1[0], rec1[2]]
        h1.sort()
        h2 = [rec2[0], rec2[2]]
        h2.sort()
        v1 = [rec1[1], rec1[3]]
        v1.sort()
        v2 = [rec2[1], rec2[3]]
        v2.sort()

        def overlap_interval(i1, i2):
            # check interval valid
            if i1[0] == i1[1] or i2[0] == i2[1]:
                return False

            # check interval overlap
            if i1[0] <= i2[0] <= i1[1] or i2[0] <= i1[0] <= i2[1]:
                if not (i1[0] < i1[1] == i2[0] < i2[1] or i2[0] < i2[1] == i1[0] < i1[1]):
                    return True
            return False

        return overlap_interval(h1, h2) and overlap_interval(v1, v2)

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candy_set = set()
        for i in range(len(candies)):
            candy_set.add(candies[i])
        return min(len(candies) // 2, len(candy_set))

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [0 for _ in range(len(nums) + 3)]
        max_num = 0
        for i in range(len(nums)):
            a[i + 3] = nums[i] + max(a[i], a[i + 1])
            max_num = max(max_num, a[i + 3])
        return max_num


def main():
    s = Solution()
    print(s.rob([2, 7, 9, 3, 1]))


if __name__ == '__main__':
    main()

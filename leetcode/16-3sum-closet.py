class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums = sorted(nums)
        res = nums[0] + nums[1] + nums[-1]

        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                change = s - target
                if change < 0:
                    l += 1
                elif change > 0:
                    r -= 1
                else:
                    return s
        return res


solution = Solution()
result = solution.threeSumClosest([-1, 2, 1, -4], 1)
print(result)

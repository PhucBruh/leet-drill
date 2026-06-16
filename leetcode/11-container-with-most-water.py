class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_arena, l, r = 0, 0, len(height) - 1

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = h * w
            if area > max_arena:
                max_arena = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_arena


solution = Solution()
result = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)

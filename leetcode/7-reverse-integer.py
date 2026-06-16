class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        i = abs(x)
        result = 0
        while i > 0:
            digit = i % 10
            i = i // 10
            result = result * 10 + digit
            # if digit != 0:

        return result * sign


solution = Solution()
print(solution.reverse(1534236469))

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        row = 0
        direction = 1
        for c in s:
            rows[row] += c

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        return "".join(rows)


solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))

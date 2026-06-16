class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        special = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        i = 0
        while i < len(s):
            if s[i : i + 2] in special:
                result += special[s[i : i + 2]]
                i = i + 2
            else:
                result += roman[s[i]]
                i += 1
            # print(result)

        return result


solution = Solution()
result = solution.romanToInt("MCMXCIV")
print(result)

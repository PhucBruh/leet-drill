# approach stack + hash
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n % 2 != 0:
            return False
        match = {")": "(", "]": "[", "}": "{"}
        box = []

        for char in s:
            if char in match:  # is close of pair
                if len(box) == 0 or box[-1] != match[char]:
                    return False
                box.pop()
            else:
                box.append(char)

        return not box


solution = Solution()
result = solution.isValid("()")
print(result)

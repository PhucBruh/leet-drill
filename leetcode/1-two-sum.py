class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        h = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in h:
                return [h[diff], i]
            h[num] = i


if __name__ == "__main__":
    # solution = Solution()
    nums = [1, 4, 8, 5, 3, 7]
    target = 10
    for i in nums:
        tmp = target - i
        # print(tmp)
        for j in nums:
            if j == tmp and i != j:
                print(i, j)
                break

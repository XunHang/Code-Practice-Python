class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0]
        for i in nums:
            curSum = max(i, curSum + i)
            maxSum = max(curSum, maxSum)
        return maxSum


slt = Solution()
d = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(slt.maxSubArray(d))

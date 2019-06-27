class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxsum = nums[0]
        sumtillhere = nums[0]

        for i in range(1, len(nums)):
            sumtillhere = max(sumtillhere + nums[i], nums[i])
            maxsum = max(maxsum, sumtillhere)

        return maxsum

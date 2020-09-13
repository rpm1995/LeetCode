class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #         ans = -float('inf')
        #         sum_ = -float('inf')

        #         for index, element in enumerate(nums):

        #             sum_ = max(sum_ + element, element)
        #             ans = max(ans, sum_)

        #         return ans

        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i] + dp[i - 1], nums[i])

        return max(dp)

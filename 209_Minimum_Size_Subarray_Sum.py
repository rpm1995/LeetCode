class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        ans = float('inf')
        left = 0
        sum_ = 0

        for right, num in enumerate(nums):

            sum_ += num

            while left <= right and sum_ >= s:
                ans = min(ans, right - left + 1)

                left_val = nums[left]
                sum_ -= left_val
                left += 1

        return ans if ans != float('inf') else 0

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = nums[0]
        max_ = min_ = nums[0]

        for num in nums[1:]:

            if num < 0:
                max_, min_ = min_, max_

            max_ = max(num, max_ * num)
            min_ = min(num, min_ * num)

            ans = max(ans, max_)

        return ans

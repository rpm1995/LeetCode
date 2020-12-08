class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        def getSubarray(target):

            left = 0
            sum_ = 0
            res = 0

            for right, value in enumerate(nums):

                sum_ += value

                while left < right and sum_ > target:
                    sum_ -= nums[left]
                    left += 1

                if sum_ == target:
                    res = max(res, right - left + 1)

            return res

        total_sum = sum(nums)

        if total_sum == x:
            return len(nums)

        length = getSubarray(total_sum - x)

        if length == 0:
            return -1

        return len(nums) - length

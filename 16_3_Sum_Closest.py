class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        ans = float('inf')

        for index, first in enumerate(nums[:-2]):

            left = index + 1
            right = len(nums) - 1

            while left < right:

                sum_ = first + nums[left] + nums[right]

                if sum_ == target:
                    return sum_

                if abs(target - sum_) < abs(ans - target):
                    ans = sum_

                if sum_ < target:
                    left += 1
                else:
                    right -= 1

        return ans

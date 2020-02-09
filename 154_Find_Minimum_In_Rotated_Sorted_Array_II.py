class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            while left < right and nums[left] == nums[left + 1]:
                left += 1

            while right > left and nums[right] == nums[right - 1]:
                right -= 1

            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid

            else:
                left = mid + 1

        return nums[right]

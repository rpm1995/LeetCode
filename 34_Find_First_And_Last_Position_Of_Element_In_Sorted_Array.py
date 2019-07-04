class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums) - 1
        ans1 = -1
        ans2 = -1

        if not nums:
            return [ans1, ans2]

        while left < right:

            mid = (left + right) // 2

            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if nums[left] != target:
            return [ans1, ans2]

        else:
            ans1 = left

        right = len(nums) - 1

        while left < right:

            mid = ((left + right) // 2) + 1

            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        ans2 = left

        return [ans1, ans2]

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        ans = len(nums)
        index = 0

        while index < len(nums):

            while index < len(nums) and nums[index] == index:
                index += 1

            while index < len(nums) and nums[index] != index and nums[index] < len(nums):
                idx = index
                a = nums[idx]
                b = nums[nums[idx]]
                nums[idx] = b
                nums[a] = a

            index += 1

        for index, val in enumerate(nums):

            if index != val:
                return index

        return ans

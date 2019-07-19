class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        #         if len(nums) == 1:
        #             return 1 if nums[0] != 1 else 2

        #         if len(nums) == 2:
        #             if 1 not in nums:
        #                 return 1

        #             if 2 not in nums:
        #                 return 2

        #             return 3

        for index in range(len(nums)):

            while 0 < nums[index] <= len(nums) and nums[index] - 1 != index:

                if nums[index] == nums[nums[index] - 1]:  # Cases like [1,3,3]
                    break
                temp = nums[nums[index] - 1]
                nums[nums[index] - 1] = nums[index]
                nums[index] = temp

        for index, number in enumerate(nums):
            if number - 1 != index:
                return index + 1

        return len(nums) + 1

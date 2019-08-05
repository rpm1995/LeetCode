class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        next_is_greater = True

        for index, number in enumerate(nums[:-1]):

            if next_is_greater:
                if nums[index + 1] < nums[index]:
                    nums[index], nums[index + 1] = nums[index + 1], nums[index]

            else:
                if nums[index + 1] > nums[index]:
                    nums[index], nums[index + 1] = nums[index + 1], nums[index]

            next_is_greater = not next_is_greater

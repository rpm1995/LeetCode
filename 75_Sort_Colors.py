class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #         zeros = 0
        #         ones = 0
        #         twos = len(nums) - 1

        #         while ones <= twos:

        #             element = nums[ones]

        #             if element == 1:
        #                 ones += 1

        #             elif element == 2:
        #                 temp = nums[ones]
        #                 nums[ones] = nums[twos]
        #                 nums[twos] = temp
        #                 # nums[ones], nums[twos] = nums[twos], nums[ones]
        #                 twos -= 1
        #                 # ones += 1

        #             elif element == 0:
        #                 temp = nums[ones]
        #                 nums[ones] = nums[zeros]
        #                 nums[zeros] = temp
        #                 # nums[ones], nums[zeros] = nums[zeros], nums[ones]
        #                 zeros += 1
        #                 ones += 1

        zeros = 0
        twos = len(nums) - 1
        curr = 0

        while curr <= twos:

            num = nums[curr]

            if nums[curr] == 0:
                nums[zeros], nums[curr] = nums[curr], nums[zeros]
                zeros += 1
                curr += 1

            elif nums[curr] == 2:
                nums[twos], nums[curr] = nums[curr], nums[twos]
                twos -= 1
                # curr += 1

            else:
                curr += 1

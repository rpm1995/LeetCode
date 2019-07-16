class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeros = 0
        ones = 0
        twos = len(nums) - 1

        while ones <= twos:

            element = nums[ones]

            if element == 1:
                ones += 1

            elif element == 2:
                temp = nums[ones]
                nums[ones] = nums[twos]
                nums[twos] = temp
                twos -= 1
                # ones += 1

            elif element == 0:
                temp = nums[ones]
                nums[ones] = nums[zeros]
                nums[zeros] = temp
                zeros += 1
                ones += 1

            # print("zeros: " + str(zeros))
            # print("ones: " + str(ones))
            # print("element: " + str(element))
            # print("twos: " + str(twos))
            # print(nums)

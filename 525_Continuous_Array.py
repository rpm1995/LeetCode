class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        #         for index, num in enumerate(nums):
        #             if num == 0:
        #                 nums[index] = -1

        #         ans = 0

        #         for i in range(len(nums)):
        #             sum_ = 0

        #             for j in range(i, len(nums)):
        #                 sum_ += nums[j]

        #                 if sum_ == 0:
        #                     ans = max(ans, j - i + 1)

        #         return ans

        seen = {0: -1}
        running_count = 0
        ans = 0

        for index, num in enumerate(nums):

            if num == 0:
                running_count -= 1
            else:
                running_count += 1

            if running_count in seen:
                ans = max(ans, index - seen[running_count])
            else:
                seen[running_count] = index

        return ans

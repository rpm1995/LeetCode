class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        ans = []

        for index, number in enumerate(nums):

            proxy_index = abs(number) - 1

            if nums[proxy_index] < 0:
                ans.append(abs(number))

            nums[proxy_index] *= -1

        return ans

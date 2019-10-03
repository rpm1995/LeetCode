class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cumsum = 0
        prefixes = {0: 1}
        ans = 0

        for index, value in enumerate(nums):

            cumsum += value

            difference = cumsum - k

            if difference in prefixes:
                ans += prefixes[difference]

            if cumsum not in prefixes:
                prefixes[cumsum] = 0
            prefixes[cumsum] += 1

        return ans

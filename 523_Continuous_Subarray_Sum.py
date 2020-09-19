class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        cumsum = [0 for _ in range(n + 1)]

        for index, num in enumerate(nums):
            cumsum[index + 1] = cumsum[index] + nums[index]

        for start in range(n):
            for end in range(start + 2, n + 1):

                if (cumsum[end] - cumsum[start] == 0 and k == 0) or (k != 0 and (cumsum[end] - cumsum[start]) % k == 0):
                    return True

        return False

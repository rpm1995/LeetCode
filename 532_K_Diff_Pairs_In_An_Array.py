class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums.sort()
        left = 0
        right = 1
        ans = 0
        n = len(nums)

        while left < n and right < n:

            if left == right or nums[right] - nums[left] < k:
                right += 1

            elif nums[right] - nums[left] > k:
                left += 1

            else:
                ans += 1

                left += 1
                while left < n and nums[left] == nums[left - 1]:
                    left += 1

        return ans

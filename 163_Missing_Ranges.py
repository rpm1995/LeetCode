class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        ans = []

        if not nums:
            if lower == upper:
                ans.append(str(lower))
            else:
                ans.append(str(lower) + "->" + str(upper))

            return ans

        if nums[0] == lower + 1:
            ans.append(str(lower))
        elif nums[0] > lower:
            ans.append(str(lower) + "->" + str(nums[0] - 1))

        for first in range(len(nums) - 1):
            if nums[first] + 1 == nums[first + 1] or nums[first] == nums[first + 1]:  # Second or for annoying test case
                continue

            if nums[first + 1] - nums[first] == 2:
                ans.append(str(nums[first] + 1))

            else:
                ans.append(str(nums[first] + 1) + "->" + str(nums[first + 1] - 1))

        if nums[-1] != upper:
            if nums[-1] == upper - 1:
                ans.append(str(upper))
            else:
                ans.append(str(nums[-1] + 1) + "->" + str(upper))

        return ans

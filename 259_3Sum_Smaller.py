class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        nums.sort()
        ans = 0

        for i, i_val in enumerate(nums):

            j = i + 1
            k = len(nums) - 1

            while j < k:

                j_val = nums[j]
                k_val = nums[k]

                if i_val + j_val + k_val < target:
                    ans += k - j  # Count (j, k), (j, k-1), ... (j, j+1)
                    j += 1

                elif i_val + j_val + k_val >= target:
                    k -= 1

        return ans

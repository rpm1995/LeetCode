class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [-1 for _ in range(n)]

        for i in range(len(nums)):
            current_num = nums[i]

            for j in range(len(nums)):
                next_num = nums[(i + j) % n]

                if next_num > current_num:
                    ans[i] = next_num
                    break

        return ans

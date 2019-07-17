class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        lengths = [1 for _ in range(len(nums))]
        ans = 1

        for cur_index, cur_element in enumerate(nums):

            for pre_index, pre_element in enumerate(nums[:cur_index]):

                if pre_element < cur_element:
                    lengths[cur_index] = max(lengths[cur_index], lengths[pre_index] + 1)
                    ans = max(ans, lengths[cur_index])

        return ans

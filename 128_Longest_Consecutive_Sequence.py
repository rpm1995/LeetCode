class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set(nums)
        ans = 0

        for num in nums:

            if num - 1 not in nums_set:  # This one single line guarantees linear time
                temp_ans = 1

                while num + 1 in nums_set:
                    temp_ans += 1
                    num += 1

                ans = max(ans, temp_ans)

        return ans

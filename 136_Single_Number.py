class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        xor = nums[0]

        for i in nums[1:]:
            xor ^= i

        return xor

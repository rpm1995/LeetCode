class Solution:

    def reverse(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n

        self.reverse(n - k, n - 1, nums)
        self.reverse(0, n - k - 1, nums)
        self.reverse(0, n - 1, nums)

#         while k:

#             last = nums[-1]

#             for index in range(len(nums)-1, 0, -1):

#                 nums[index] = nums[index-1]

#             nums[0] = last
#             k -= 1


#         temp = nums[:]
#         n = len(nums)

#         for index, value in enumerate(temp):

#             nums[(index + k) % n] = value

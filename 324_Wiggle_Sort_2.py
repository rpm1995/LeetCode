class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        ans = nums[:]

        for i in range(1, len(nums), 2):
            nums[i] = ans.pop()

        for i in range(0, len(nums), 2):
            nums[i] = ans.pop()


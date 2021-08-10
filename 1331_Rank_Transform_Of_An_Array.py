class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        nums = sorted(list(set(arr)))
        dicti = {}

        for index, num in enumerate(nums):
            dicti[num] = index + 1

        for index, val in enumerate(arr):
            arr[index] = dicti[val]

        return arr

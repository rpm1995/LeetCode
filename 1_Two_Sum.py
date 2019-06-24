class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dicti = {}

        for index, element in enumerate(nums):
            to_find = target - element

            if to_find in dicti:
                return [index, dicti[to_find]]

            dicti[element] = index

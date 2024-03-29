# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#
#         tortoise = nums[0]
#         hare = nums[0]
#
#         while True:
#
#             tortoise = nums[tortoise]
#             hare = nums[hare]
#             hare = nums[hare]
#
#             if tortoise == hare:
#                 break
#
#         hare = nums[0]
#
#         while hare != tortoise:
#             hare = nums[hare]
#             tortoise = nums[tortoise]
#
#         return hare

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        while True:

            temp = nums[0]

            if nums[temp] == temp:
                return temp

            nums[0] = nums[temp]
            nums[temp] = temp

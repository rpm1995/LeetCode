# class Solution:                                   # Timeout for LAST test case
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#
#         first_number = {}
#         ans = []
#         ans_set = set()
#
#         for index, num in enumerate(nums):
#             if num not in first_number:
#                 first_number[num] = []
#             first_number[num].append(index)
#
#         for second in range(len(nums)):
#             for third in range(second + 1, len(nums)):
#
#                 second_number = nums[second]
#                 third_number = nums[third]
#
#                 need = -second_number - third_number
#
#                 if need in first_number:
#                     for values in first_number[need]:
#                         if values != second and values != third:
#                             to_add = sorted((second_number, third_number, need))
#                             ans_set.add(tuple(to_add))
#
#         ans_set = [list(elements) for elements in ans_set]
#         return ans_set

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        ans = []
        first = 0

        while first < len(nums) - 2:

            if first > 0 and nums[first] == nums[first - 1]:  # Duplicates for first
                first += 1
                continue

            second = first + 1
            third = len(nums) - 1

            while second < third:
                sum_ = nums[first] + nums[second] + nums[third]

                if sum_ == 0:
                    ans.append([nums[first], nums[second], nums[third]])

                    while second < third and nums[second] == nums[second + 1]:  # Duplicates for second
                        second += 1
                    while third > second and nums[third] == nums[third - 1]:  # Duplicates for third
                        third -= 1
                    second += 1
                    third -= 1

                elif sum_ > 0:
                    third -= 1

                elif sum_ < 0:
                    second += 1
            first += 1

        return ans

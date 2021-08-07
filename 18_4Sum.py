class Solution:

    def get_sum(self, ptr_1, ptr_2, ptr_3, ptr_4, nums):

        return nums[ptr_1] + nums[ptr_2] + nums[ptr_3] + nums[ptr_4]

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        ptr_1 = 0
        ans = []

        while ptr_1 < len(nums):

            while ptr_1 > 0 and ptr_1 < len(nums) and nums[ptr_1] == nums[ptr_1 - 1]:
                ptr_1 += 1

            ptr_2 = ptr_1 + 1

            # while ptr_2 > ptr_1 + 1 and nums[ptr_2] == nums[ptr_2 - 1] and ptr_2 < len(nums):
            #     ptr_2 += 1

            while ptr_2 < len(nums):

                while ptr_2 > ptr_1 + 1 and ptr_2 < len(nums) and nums[ptr_2] == nums[ptr_2 - 1]:
                    ptr_2 += 1

                ptr_3 = ptr_2 + 1
                ptr_4 = len(nums) - 1

                while ptr_3 < ptr_4:

                    sum_ = self.get_sum(ptr_1, ptr_2, ptr_3, ptr_4, nums)
                    third_number = nums[ptr_3]
                    fourth_number = nums[ptr_4]

                    if sum_ == target:
                        ans.append([nums[ptr_1], nums[ptr_2], nums[ptr_3], nums[ptr_4]])

                    if sum_ <= target:
                        while ptr_3 < ptr_4 and nums[ptr_3] == third_number:
                            ptr_3 += 1

                    elif sum_ > target:
                        while ptr_4 > ptr_3 and nums[ptr_4] == fourth_number:
                            ptr_4 -= 1

                ptr_2 += 1

            ptr_1 += 1

        return ans

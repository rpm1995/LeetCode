class Solution:
    def canJump(self, nums: List[int]) -> bool:

        can_reach = [False for _ in range(len(nums))]
        can_reach[-1] = True
        cur_max = len(nums) - 1

        for current in range(len(nums) - 2, -1, -1):

            if nums[current] + current >= len(nums) or nums[current] + current >= cur_max:
                can_reach[current] = True
                cur_max = current

        # print(can_reach)
        return can_reach[0]

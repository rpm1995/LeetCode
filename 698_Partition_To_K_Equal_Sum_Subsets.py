class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        def helper(res, visited, k, next_index):

            # if res > required_subset_sum:
            #     return False

            if k == 0:
                return True

            if res == required_subset_sum:
                return helper(0, visited, k - 1, 0)

            for i in range(next_index, n):

                if not visited[i] and res + nums[i] <= required_subset_sum:
                    visited[i] = True
                    explore = helper(res + nums[i], visited, k, i + 1)

                    if explore:
                        return True

                    visited[i] = False

            return False

        n = len(nums)
        required_subset_sum = sum(nums) // k

        if sum(nums) % k != 0 or required_subset_sum < max(nums):
            return False

        return helper(0, [False for _ in range(n)], k, 0)

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        #         def helper(index, res):

        #             if index == n:
        #                 if res == S:
        #                     self.ans += 1
        #                 return

        #             add = helper(index+1, res+nums[index])
        #             subtract = helper(index+1, res-nums[index])

        #             return

        #         n = len(nums)
        #         self.ans = 0
        #         helper(0, 0)

        #         return self.ans

        def helper(index, res, cache):
            # cache values hold NUMBER of ways from this point
            if (index, res) in cache:
                return cache[(index, res)]

            if index == n:
                if res == S:
                    cache[(index, res)] = 1
                else:
                    cache[(index, res)] = 0

                return cache[(index, res)]

            add = helper(index + 1, res + nums[index], cache)
            subtract = helper(index + 1, res - nums[index], cache)

            cache[(index, res)] = add + subtract

            return cache[(index, res)]

        cache = {}
        n = len(nums)
        return helper(0, 0, cache)

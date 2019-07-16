class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def helper(ans, res, nums):

            if not nums:
                ans.append(res[:])

            else:

                element = nums.pop()
                helper(ans, res, nums)
                res.append(element)
                helper(ans, res, nums)
                res.pop()
                nums.append(element)

            return ans

        return helper([], [], nums)

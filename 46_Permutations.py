class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(ans, res, nums):

            if not nums:
                ans.append(res[:])
                return

            else:

                for index, element in enumerate(nums):
                    nums.pop(index)
                    res.append(element)
                    helper(ans, res, nums)
                    res.pop()
                    nums.insert(index, element)

                return

        self.ans = []

        if not nums:
            return self.ans

        helper(self.ans, [], nums)
        return self.ans

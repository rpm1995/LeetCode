class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def helper(numbers, sum_so_far, res, cur_number):

            if numbers == k and sum_so_far + cur_number == n:
                print(sum_so_far)
                self.ans.append(res[:])
                return

            if numbers >= k or sum_so_far + cur_number >= n:
                return

            if numbers < k:
                for number in range(cur_number + 1, 10):
                    res.append(number)
                    helper(numbers + 1, sum_so_far + cur_number, res, number)
                    res.pop()

        self.ans = []
        helper(0, 0, [], 0)
        return self.ans

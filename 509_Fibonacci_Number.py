class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """

        def helper(n):

            if n == 1:
                return 1
            elif n == 0:
                return 0

            return helper(n - 1) + helper(n - 2)

        return helper(N)

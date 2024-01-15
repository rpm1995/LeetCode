class Solution(object):
    def fib(self, n: int) -> int:

        if n == 0: return 0
        if n == 1: return 1

        firstTerm = 0
        secondTerm = 1
        n -= 1

        nthTerm = firstTerm + secondTerm

        while n:
            nthTerm = firstTerm + secondTerm
            firstTerm = secondTerm
            secondTerm = nthTerm

            n-= 1
        
        return nthTerm
        
    # def fib(self, N):
    #     """
    #     :type N: int
    #     :rtype: int
    #     """

    #     def helper(n):

    #         if n == 1:
    #             return 1
    #         elif n == 0:
    #             return 0

    #         return helper(n - 1) + helper(n - 2)

    #     return helper(N)

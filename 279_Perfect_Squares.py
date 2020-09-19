class Solution:
    def numSquares(self, n: int) -> int:

        def helper(n):

            if n in squares:
                return 1

            ans = float('inf')
            for square in squares:
                possible_answer = helper(n - square) + 1
                ans = min(ans, possible_answer)

            return ans

        squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        return helper(n)

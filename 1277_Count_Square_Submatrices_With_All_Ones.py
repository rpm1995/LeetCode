class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        ans = 0

        for i in range(rows):
            dp[i][0] = matrix[i][0]
            ans += dp[i][0]

        for j in range(cols):
            dp[0][j] = matrix[0][j]
            ans += dp[0][j]

        ans -= dp[0][0]

        for i in range(1, rows):
            for j in range(1, cols):

                if matrix[i][j] != 0:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

                ans += dp[i][j]

        return ans

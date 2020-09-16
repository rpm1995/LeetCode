class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):

                if row == 0:
                    if col == 0:
                        dp[row][col] = grid[row][col]
                    else:
                        dp[row][col] = grid[row][col] + dp[row][col - 1]

                elif col == 0:
                    dp[row][col] = grid[row][col] + dp[row - 1][col]

                else:
                    dp[row][col] = grid[row][col] + min(dp[row][col - 1], dp[row - 1][col])

        return dp[-1][-1]

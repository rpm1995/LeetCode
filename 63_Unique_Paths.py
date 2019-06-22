class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = 1

        for i in range(1, cols):
            if obstacleGrid[0][i] == 0 and dp[0][i - 1] == 1:
                dp[0][i] = 1

        for j in range(1, rows):
            if obstacleGrid[j][0] == 0 and dp[j - 1][0] == 1:
                dp[j][0] = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # for row in range(rows):
        #     for col in range(cols):
        #         print(dp[row][col])
        #     print("\n")

        return dp[-1][-1]

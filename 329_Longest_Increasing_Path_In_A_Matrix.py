class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:
            return 0

        memo = {}
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


        def dfs(curr_x, curr_y):

            if (curr_x, curr_y) in memo:
                return memo[(curr_x, curr_y)]

            length = 0

            for dx, dy in directions:

                new_x = curr_x + dx
                new_y = curr_y + dy

                if 0 <= new_x < rows and 0 <= new_y < cols and matrix[new_x][new_y] > matrix[curr_x][curr_y]:
                    length = max(length, dfs(new_x, new_y))

            length += 1
            memo[(curr_x, curr_y)] = length

            return memo[(curr_x, curr_y)]


        for row in range(rows):
            for col in range(cols):
                ans = max(ans, dfs(row, col))

        return ans

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        def helper(grid, curr_x, curr_y):

            grid[curr_x][curr_y] = "X"

            for dx, dy in directions:

                new_x = curr_x + dx
                new_y = curr_y + dy

                if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == "1":
                    helper(grid, new_x, new_y)

        ans = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    helper(grid, row, col)
                    ans += 1

        return ans

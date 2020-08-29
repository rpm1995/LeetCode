from collections import deque


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def flood_fill(grid, row, col):

            if grid[row][col] == 1:
                return

            queue = deque([])
            queue.append((row, col))

            while queue:

                curr_x, curr_y = queue.popleft()
                grid[curr_x][curr_y] = 1

                for dx, dy in directions:
                    new_x = curr_x + dx
                    new_y = curr_y + dy

                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 0:
                        queue.append((new_x, new_y))

            return

        def set_border_lands(grid):

            for col in range(cols):
                flood_fill(grid, 0, col)
                flood_fill(grid, rows - 1, col)

            for row in range(rows):
                flood_fill(grid, row, 0)
                flood_fill(grid, row, cols - 1)

            return

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        ans = 0
        set_border_lands(grid)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    ans += 1
                    flood_fill(grid, row, col)

        return ans

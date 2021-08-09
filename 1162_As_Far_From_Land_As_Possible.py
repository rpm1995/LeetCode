from collections import deque


class Solution:

    def get_land_coordinates(self, arr):

        for row in range(self.rows):
            for col in range(self.cols):

                if self.grid[row][col] == 1:
                    arr.append([row, col, 0])

    def get_max(self):

        ans = 0

        for row in range(self.rows):
            for col in range(self.cols):
                ans = max(ans, self.grid[row][col])

        return ans

    def maxDistance(self, grid: List[List[int]]) -> int:

        queue = []
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.get_land_coordinates(queue)
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        if len(queue) == self.rows * self.cols or len(queue) == 0:
            return -1

        queue = deque(queue)

        while queue:

            curr_x, curr_y, dist = queue.popleft()

            for dx, dy in directions:
                new_x = curr_x + dx
                new_y = curr_y + dy

                if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                    if grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = dist + 1
                        queue.append([new_x, new_y, grid[new_x][new_y]])

        ans = self.get_max()
        return ans

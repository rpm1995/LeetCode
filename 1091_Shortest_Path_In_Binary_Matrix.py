from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1

        queue = deque([])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        n = len(grid)
        visited = set()

        queue.append((0, 0, 1))

        while queue:

            curr_x, curr_y, length = queue.popleft()

            if (curr_x, curr_y) == (n - 1, n - 1):
                return length

            for dx, dy in directions:
                new_x = curr_x + dx
                new_y = curr_y + dy

                if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                    if (new_x, new_y) not in visited:
                        queue.append((new_x, new_y, length + 1))
                        visited.add((new_x, new_y))  # Times out without this line

            # visited.add((curr_x, curr_y))

        return -1

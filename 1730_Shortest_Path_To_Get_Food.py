from collections import deque


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        def getStart(grid):

            for row in range(rows):
                for col in range(cols):

                    if grid[row][col] == "*":
                        return row, col

        def bfs(x, y, dist=0):

            queue = deque([(x, y, 0)])
            visited.add((x, y))

            while queue:

                curr_x, curr_y, dist = queue.popleft()
                # visited.add((curr_x, curr_y))

                if grid[curr_x][curr_y] == "#":
                    return dist

                dist += 1

                for dx, dy in directions:

                    new_x = curr_x + dx
                    new_y = curr_y + dy

                    if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited and grid[new_x][
                        new_y] != "X":
                        queue.append((new_x, new_y, dist))
                        visited.add((new_x, new_y))

            return -1

        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()

        x, y = getStart(grid)
        ans = bfs(x, y, 0)

        return ans

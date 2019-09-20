from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        fresh = set()
        rotten = set()
        queue = deque([])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh.add((row, col))
                elif grid[row][col] == 2:
                    queue.append((row, col, 0))

        while queue:

            curr_x, curr_y, depth = queue.popleft()
            ans = max(ans, depth)

            if (curr_x, curr_y) in rotten:
                continue

            for dx, dy in directions:
                new_x = curr_x + dx
                new_y = curr_y + dy

                if (new_x, new_y) in rotten:
                    continue
                elif (new_x, new_y) in fresh:
                    fresh.remove((new_x, new_y))
                    queue.append((new_x, new_y, depth + 1))

            rotten.add((curr_x, curr_y))

        if fresh:
            return - 1
        return ans

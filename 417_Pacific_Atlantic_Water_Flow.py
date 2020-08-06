class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        pacific_possible = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic_possible = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        ans = []

        def dfs(curr_x, curr_y, visited):

            visited[curr_x][curr_y] = True
            curr_val = matrix[curr_x][curr_y]

            for dx, dy in directions:

                new_x = curr_x + dx
                new_y = curr_y + dy

                if 0 <= new_x < rows and 0 <= new_y < cols and matrix[new_x][new_y] >= curr_val and visited[new_x][
                    new_y] is False:
                    dfs(new_x, new_y, visited)

            return

        for col in range(cols):
            dfs(0, col, pacific_possible)
            dfs(rows - 1, col, atlantic_possible)

        for row in range(rows):
            dfs(row, 0, pacific_possible)
            dfs(row, cols - 1, atlantic_possible)

        for row in range(rows):
            for col in range(cols):
                if atlantic_possible[row][col] and pacific_possible[row][col]:
                    ans.append([row, col])

        return ans

    #BFS:

    from collections import deque

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:

        if not matrix:
            return []

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        rows = len(matrix)
        cols = len(matrix[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        ans = []

        def bfs(curr_x, curr_y, reachable):

            queue = deque([])
            queue.append((curr_x, curr_y))
            reachable.add((curr_x, curr_y))

            while queue:

                curr_x, curr_y = queue.popleft()

                for dx, dy in directions:

                    new_x = curr_x + dx
                    new_y = curr_y + dy

                    if 0 <= new_x < rows and 0 <= new_y < cols and matrix[new_x][new_y] >= matrix[curr_x][
                        curr_y] and (new_x, new_y) not in reachable:
                        queue.append((new_x, new_y))
                        reachable.add((new_x, new_y))

            return

        for col in range(cols):
            bfs(0, col, pacific_reachable)
            bfs(rows - 1, col, atlantic_reachable)

        for row in range(rows):
            bfs(row, 0, pacific_reachable)
            bfs(row, cols - 1, atlantic_reachable)

        print(pacific_reachable)
        print(atlantic_reachable)

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_reachable and (row, col) in atlantic_reachable:
                    ans.append([row, col])

        return ans


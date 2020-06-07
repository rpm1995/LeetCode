from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def get_gates(queue, rooms):

            for row in range(rows):
                for col in range(cols):
                    if rooms[row][col] == 0:
                        queue.append((row, col, 0))

            return

        def bfs(queue, rooms):

            visited = set()

            while queue:

                curr_x, curr_y, distance = queue.popleft()

                for dx, dy in directions:
                    new_x = curr_x + dx
                    new_y = curr_y + dy

                    if 0 <= new_x < rows and 0 <= new_y < cols and rooms[new_x][new_y] != -1 and rooms[new_x][
                        new_y] != 0 and (new_x, new_y) not in visited:
                        rooms[new_x][new_y] = distance + 1
                        queue.append((new_x, new_y, distance + 1))
                        visited.add((new_x, new_y))

            return

        if not rooms:
            return

        rows = len(rooms)
        cols = len(rooms[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = deque([])
        get_gates(queue, rooms)
        bfs(queue, rooms)

        return

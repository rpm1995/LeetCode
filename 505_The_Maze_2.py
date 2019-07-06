from collections import deque


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        rows = len(maze)
        cols = len(maze[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = deque([])
        destx = destination[0]
        desty = destination[1]
        visited = {}

        queue.append((start[0], start[1], 0))
        visited[(start[0], start[1])] = 0

        while queue:

            curr_x, curr_y, curdistance = queue.popleft()

            # if (curr_x, curr_y) == (destx, desty):
            #     return curdistance

            for dx, dy in directions:
                distance = 1
                newx = curr_x + dx
                newy = curr_y + dy

                while 0 <= newx < rows and 0 <= newy < cols and maze[newx][newy] != 1:
                    newx += dx
                    newy += dy
                    distance += 1

                newx -= dx
                newy -= dy
                distance -= 1

                if (newx, newy) not in visited or visited[(newx, newy)] > curdistance + distance:
                    visited[(newx, newy)] = curdistance + distance
                    visited[(newx, newy)] = min(visited[(newx, newy)], curdistance + distance)

                    queue.append((newx, newy, curdistance + distance))


        if (destx, desty) not in visited:
            return -1
        return visited[(destx, desty)]

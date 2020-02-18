import heapq


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:

        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        rows = len(A)
        cols = len(A[0])
        visited = set()

        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (-A[0][0], 0, 0))
        visited.add((0, 0))

        while heap:
            value, cur_x, cur_y = heapq.heappop(heap)

            if cur_x == rows - 1 and cur_y == cols - 1:
                return -value

            for dx, dy in directions:
                new_x = cur_x + dx
                new_y = cur_y + dy

                if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
                    heapq.heappush(heap, (max(value, -A[new_x][new_y]), new_x, new_y))
                    visited.add((new_x, new_y))
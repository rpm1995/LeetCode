import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap = []
        heapq.heapify(heap)
        element = 0

        for col in range(len(matrix[0])):
            heapq.heappush(heap, (matrix[0][col], 0, col))

        while k:

            element, row, col = heapq.heappop(heap)

            if row < len(matrix) - 1:
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))

            k -= 1

        return element

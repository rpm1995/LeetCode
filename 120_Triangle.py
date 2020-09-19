class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        rows = len(triangle)

        for row in range(rows - 2, -1, -1):
            cols = len(triangle[row])

            for col in range(cols):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        return triangle[0][0]

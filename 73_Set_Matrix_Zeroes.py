class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        firstrowzeros = False
        firstcolzeros = False
        rows = len(matrix)
        cols = len(matrix[0])

        for element in matrix[0]:
            if element == 0:
                firstrowzeros = True
                break

        for row in range(rows):
            if matrix[row][0] == 0:
                firstcolzeros = True
                break

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(1, rows):
                    matrix[row][col] = 0

        for row in range(1, rows):
            if matrix[row][0] == 0:
                for col in range(1, cols):
                    matrix[row][col] = 0

        if firstrowzeros:
            for col in range(cols):
                matrix[0][col] = 0

        if firstcolzeros:
            for row in range(rows):
                matrix[row][0] = 0

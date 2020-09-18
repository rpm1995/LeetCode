class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def get_maximal_square_length(i, j):

            square_length = 1
            all_ones = True

            while i + square_length < rows and j + square_length < cols and all_ones:

                for k in range(i, i + square_length + 1):
                    if matrix[k][j + square_length] == "0":                 # Why?
                        all_ones = False
                        break

                for k in range(j, j + square_length + 1):
                    if matrix[i + square_length][k] == "0":                 # Why?
                        all_ones = False
                        break

                if all_ones:
                    square_length += 1

            return square_length

        if not matrix:
            return 0

        max_square_side = 0
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):

                if matrix[i][j] == "1":
                    square_length = get_maximal_square_length(i, j)
                    max_square_side = max(max_square_side, square_length)

        return max_square_side ** 2

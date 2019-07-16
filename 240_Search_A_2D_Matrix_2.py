class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        row = rows - 1
        col = 0

        while 0 <= row < rows and 0 <= col < cols:

            element = matrix[row][col]

            if element == target:
                return True

            elif element < target:
                col += 1

            elif element > target:
                row -= 1

        return False

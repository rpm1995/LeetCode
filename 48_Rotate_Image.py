class Solution:

    def transpose(self, matrix):

        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse(self, matrix):

        for i in range(self.rows):
            for j in range(self.cols // 2):
                matrix[i][j], matrix[i][self.cols - j - 1] = matrix[i][self.cols - j - 1], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.transpose(matrix)
        self.reverse(matrix)

#         n = len(matrix)

#         for i in range(n - (n//2)):
#             for j in range(i, n - i - 1):

#                 temp = matrix[i][j]
#                 matrix[i][j] = matrix[~j][i]
#                 matrix[~j][i] = matrix[~i][~j]
#                 matrix[~i][~j] = matrix[j][~i]
#                 matrix[j][~i] = temp

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        rows = len(board)
        cols = len(board[0])
        crush = True

        while crush:

            crush = False

            for i in range(rows):
                for j in range(cols):

                    if board[i][j] == 0:
                        continue

                    value = abs(board[i][j])

                    if i < rows - 2:

                        if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                            index = i
                            crush = True

                            while index < rows and abs(board[index][j]) == value:
                                board[index][j] = -value
                                index += 1

                    if j < cols - 2:

                        if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                            index = j
                            crush = True

                            while index < cols and abs(board[i][index]) == value:
                                board[i][index] = -value
                                index += 1

            if crush:

                for col in range(cols):
                    nonzeros = rows - 1

                    for row in range(rows - 1, -1, -1):

                        if board[row][col] > 0:
                            board[nonzeros][col] = board[row][col]
                            nonzeros -= 1

                    for row in range(nonzeros, -1, -1):
                        board[row][col] = 0

        return board

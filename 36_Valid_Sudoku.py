class Solution:

    def row_is_possible(self, curr_row, curr_y, value):

        for col in range(self.cols):

            if self.board[curr_row][col] != ".":
                if col != curr_y and int(self.board[curr_row][col]) == value:
                    return False

        return True

    def col_is_possible(self, curr_row, curr_y, value):

        for row in range(self.rows):

            if self.board[row][curr_y] != ".":
                if row != curr_row and int(self.board[row][curr_y]) == value:
                    return False

        return True

    def box_is_possible(self, curr_row, curr_col, value):

        for row in range(curr_row - (curr_row % 3), curr_row - (curr_row % 3) + 3):
            for col in range(curr_col - (curr_col % 3), curr_col - (curr_col % 3) + 3):

                if self.board[row][col] != ".":
                    if row != curr_row and col != curr_col and int(self.board[row][col]) == value:
                        return False

        return True

    def is_possible(self, curr_row, curr_y, value):

        return self.row_is_possible(curr_row, curr_y, value) and self.col_is_possible(curr_row, curr_y, value) \
               and self.box_is_possible(curr_row, curr_y, value)

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        self.board = board
        self.rows = len(self.board)
        self.cols = len(self.board[0])

        for row in range(self.rows):
            for col in range(self.cols):

                if self.board[row][col] != "." and not self.is_possible(row, col, int(self.board[row][col])):
                    return False

        return True

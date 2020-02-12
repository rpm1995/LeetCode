class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def row_win(self, player, row):

        for col in range(self.n):
            if self.board[row][col] != player:
                return False

        return True

    def col_win(self, player, col):

        for row in range(self.n):
            if self.board[row][col] != player:
                return False

        return True

    def diagonals_win(self, player, row, col):

        if row != col and row + col != self.n - 1:
            return False

        diagonal = True
        anti_diagonal = True

        for i in range(self.n):
            if self.board[i][i] != player:
                diagonal = False

        for i in range(self.n):
            if self.board[i][self.n - 1 - i] != player:
                anti_diagonal = False

        return diagonal or anti_diagonal

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player

        if self.row_win(player, row):
            return player

        if self.col_win(player, col):
            return player

        if self.diagonals_win(player, row, col):
            return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
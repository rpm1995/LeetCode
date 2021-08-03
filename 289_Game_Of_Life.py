class Solution:

    def set_value(self, curr_x, curr_y):

        live_neighbours = 0

        for dx, dy in self.directions:

            new_x = curr_x + dx
            new_y = curr_y + dy

            if 0 <= new_x < self.rows and 0 <= new_y < self.cols:

                if abs(self.board[new_x][new_y]) == 1:
                    live_neighbours += 1

        if abs(self.board[curr_x][curr_y]) == 1:

            if live_neighbours < 2:
                self.board[curr_x][curr_y] = -1
            elif live_neighbours > 3:
                self.board[curr_x][curr_y] = -1

        elif self.board[curr_x][curr_y] == 0 or self.board[curr_x][curr_y] == -2:

            if live_neighbours == 3:
                self.board[curr_x][curr_y] = -2

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.board = board
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for row in range(self.rows):
            for col in range(self.cols):
                self.set_value(row, col)

        for row in range(self.rows):
            for col in range(self.cols):

                if self.board[row][col] == -1:
                    self.board[row][col] = 0

                elif self.board[row][col] == -2:
                    self.board[row][col] = 1

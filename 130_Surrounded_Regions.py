from collections import deque


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        queue = deque([])
        rows = len(board)
        cols = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Collect border elements

        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows - 1 or col == 0 or col == cols - 1) and board[row][col] == "O":
                    queue.append((row, col))

        # Process connected border elements

        while queue:

            curr_x, curr_y = queue.popleft()
            board[curr_x][curr_y] = "*"

            for dx, dy in directions:
                new_x = curr_x + dx
                new_y = curr_y + dy

                if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] == "O":
                    queue.append((new_x, new_y))

        # Turn all remaining O's into X's

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"

        # Revert *'s back to O's

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "*":
                    board[row][col] = "O"

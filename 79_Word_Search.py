class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        rows = len(board)
        cols = len(board[0])

        def helper(board, visited, remaining, curr_x, curr_y):

            visited.add((curr_x, curr_y))

            if not remaining:
                return True

            else:
                next_char = remaining[0]

                for dx, dy in directions:
                    new_x = curr_x + dx
                    new_y = curr_y + dy

                    if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited and board[new_x][
                        new_y] == next_char:
                        if helper(board, visited, remaining[1:], new_x, new_y) is True:
                            return True

            visited.remove((curr_x, curr_y))

            return False

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == word[0]:
                    if helper(board, set(), word[1:], x, y) is True:
                        return True

        return False

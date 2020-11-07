from collections import deque


class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        def bfs(x, y, char):

            if board[x][y] == char:
                return x, y, '!'

            queue = deque([(x, y, '')])
            visited = set((x, y))

            while queue:

                x, y, path = queue.popleft()

                for dx, dy, dpath in directions:

                    new_x = x + dx
                    new_y = y + dy

                    if 0 <= new_x < rows and 0 <= new_y < len(board[new_x]) and (new_x, new_y) not in visited:

                        visited.add((new_x, new_y))

                        if board[new_x][new_y] != char:
                            queue.append((new_x, new_y, path + dpath))
                        else:
                            return new_x, new_y, path + dpath + '!'

        directions = [(-1, 0, 'U'), (0, -1, 'L'), (1, 0, 'D'), (0, 1, 'R')]
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        rows = len(board)

        curr_x, curr_y = 0, 0
        ans = ''

        for char in target:
            curr_x, curr_y, res = bfs(curr_x, curr_y, char)
            ans += res

        return ans

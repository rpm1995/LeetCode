from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        # if board == [[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]:
        #     return 2
        # elif board == [[-1,10,-1,15,-1],[-1,-1,18,2,20],[-1,-1,12,-1,-1],[2,4,11,18,8],[-1,-1,-1,-1,-1]]:
        #     return 3

        N = len(board)
        visited = set()
        new_board = []

        backward = True
        if N % 2 == 0:
            backward = False

        for i in range(N):
            rowholder = board[i]
            if backward is True:
                rowholder.reverse()

            new_board.extend(rowholder)
            backward = not backward

        new_board.reverse()
        print(new_board)

        queue = deque([])
        queue.append(0)
        visited.add(0)
        ans = 0

        while queue:

            possibilities = len(queue)

            while possibilities > 0:
                current = queue.popleft()

                if current == N ** 2 - 1:
                    return ans

                for x in range(1, 7):
                    dx = current + x

                    if dx > N ** 2 - 1:
                        continue

                    if new_board[dx] != -1:
                        dx = new_board[dx] - 1

                    if dx not in visited:
                        queue.append(dx)
                        visited.add(dx)

                possibilities -= 1

            ans += 1

        return -1

from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        start = "0000"
        deadends = set(deadends)
        queue = deque([(start, 0)])
        visited = set()

        while queue:

            current, depth = queue.popleft()

            if current in visited or current in deadends:
                continue

            if current == target:
                return depth

            visited.add(current)
            res = self.generate(current)

            for neighbour in res:
                queue.append((neighbour, depth + 1))

        return -1

    def generate(self, cur):

        res = []

        for i, val in enumerate(cur):
            res.append(cur[: i] + str((int(cur[i]) + 1) % 10) + cur[i + 1:])
            res.append(cur[: i] + str((int(cur[i]) - 1) % 10) + cur[i + 1:])

        return res

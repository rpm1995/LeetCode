class Solution:

    def dfs(self, curr_x, curr_y):

        self.seen.add((curr_x, curr_y))

        for x, y in self.stones:

            if x == curr_x or y == curr_y:
                if (x, y) not in self.seen:
                    self.dfs(x, y)

    def removeStones(self, stones: List[List[int]]) -> int:

        self.stones = stones
        self.seen = set()
        islands = 0

        for x, y in self.stones:

            if (x, y) not in self.seen:
                self.dfs(x, y)
                islands += 1

        return len(self.stones) - islands

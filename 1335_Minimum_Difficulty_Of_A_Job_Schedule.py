class Solution:

    def helper(self, jobs, d, index):

        if d == 1:
            # print(index)
            return max(jobs[index:])

        if (index, d) in self.visited:
            return self.visited[(index, d)]

        difficulty = float('inf')

        for i in range(index + 1, len(jobs)):
            # print(i)
            # print(max(jobs[index:i]))
            local_difficulty = max(jobs[index: i]) + self.helper(jobs, d - 1, i)
            difficulty = min(difficulty, local_difficulty)

        self.visited[(index, d)] = difficulty
        return difficulty

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        self.visited = {}
        ans = self.helper(jobDifficulty, d, 0)
        # print(self.visited)
        return ans if ans != float('inf') else -1

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        def manhattan(worker_index, bike_index):

            worker_x = workers[worker_index][0]
            worker_y = workers[worker_index][1]
            bike_x = bikes[bike_index][0]
            bike_y = bikes[bike_index][1]

            distance = abs(worker_x - bike_x) + abs(worker_y - bike_y)

            return distance

        def dfs(worker_index, bike_index, distance_so_far, visited):

            if worker_index == len(workers):
                self.ans = min(self.ans, distance_so_far)

            if distance_so_far >= self.ans:
                return

            for index in range(len(bikes)):

                if index not in visited:
                    visited.add(index)
                    dfs(worker_index + 1, index, distance_so_far + manhattan(worker_index, index), visited)
                    visited.remove(index)

        self.ans = float('inf')
        dfs(0, 0, 0, set())
        return self.ans

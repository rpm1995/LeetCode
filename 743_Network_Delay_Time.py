class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        adjlist = {}
        min_distances = {}

        for source, destination, time in times:
            if source not in adjlist:
                adjlist[source] = []
            adjlist[source].append((destination, time))

        for source in range(1, N + 1):
            min_distances[source] = float('inf')

        def dfs(current, distance):

            if distance >= min_distances[current]:
                return

            min_distances[current] = distance

            if current in adjlist:
                for destination, time in sorted(adjlist[current]):
                    dfs(destination, distance + time)

        dfs(K, 0)
        ans = max(min_distances.values())

        return ans if ans != float('inf') else -1

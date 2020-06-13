from collections import deque
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        #         adjlist = {}
        #         min_distances = {}

        #         for source, destination, time in times:
        #             if source not in adjlist:
        #                 adjlist[source] = []
        #             adjlist[source].append((destination, time))

        #         for source in range(1, N+1):
        #             min_distances[source] = float('inf')

        #         def dfs(current, distance):

        #             if distance >= min_distances[current]:
        #                 return

        #             min_distances[current] = distance

        #             if current in adjlist:
        #                 for destination, time in sorted(adjlist[current]):
        #                     dfs(destination, distance+time)

        #         dfs(K, 0)
        #         ans = max(min_distances.values())

        #         return ans if ans != float('inf') else -1

        # # BFS approach is inaccurate?

        #         def bfs(adjlist):

        #             queue = deque([])
        #             visited = {K: 0}
        #             ans = 0
        #             queue.append((K, 0))

        #             while queue:
        #                 print(queue)
        #                 current, distance = queue.popleft()
        #                 # maxTime = 0

        #                 for neighbour, time in adjlist[current]:
        #                     if neighbour not in visited:
        #                         visited[neighbour] = distance+time
        #                         # maxTime = max(maxTime, time)
        #                         ans += visited[neighbour]
        #                         queue.append((neighbour, visited[neighbour]))

        #                     elif visited[neighbour] > distance+time:
        #                         ans -= visited[neighbour]
        #                         visited[neighbour] = distance+time
        #                         # maxTime = max(maxTime, time)
        #                         ans += visited[neighbour]
        #                         queue.append((neighbour, visited[neighbour]))

        #                     print(ans)

        #             if len(visited) < N:
        #                 return -1

        #             return ans

        #         adjlist = {}

        #         for node in range(1, N+1):
        #             adjlist[node] = []

        #         for source, destination, time in times:
        #             adjlist[source].append([destination, time])

        #         ans = bfs(adjlist)

        #         return ans

        adjlist = {}
        min_dist = {}
        heap = []
        heapq.heapify(heap)

        for source, dest, time in times:
            if source not in adjlist:
                adjlist[source] = []
            adjlist[source].append([time, dest])

        heapq.heappush(heap, (0, K))

        while heap:

            time_to_here, cur = heapq.heappop(heap)

            if cur not in min_dist:
                min_dist[cur] = time_to_here

                if cur in adjlist:
                    for time_to_there, neighbour in adjlist[cur]:
                        heapq.heappush(heap, (time_to_here + time_to_there, neighbour))

        return max(min_dist.values()) if len(min_dist) == N else -1

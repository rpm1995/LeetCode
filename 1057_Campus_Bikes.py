import heapq


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        distances = []

        for worker, (work_x, work_y) in enumerate(workers):
            distance = []

            for bike, (bike_x, bike_y) in enumerate(bikes):
                manhattan = abs(work_x - bike_x) + abs(work_y - bike_y)
                distance.append([manhattan, worker, bike])

            distance.sort(reverse=True)
            distances.append(distance)

        queue = []
        seen = set()
        ans = [-1 for _ in range(len(workers))]

        for worker in range(len(workers)):
            queue.append(distances[worker].pop())

        heapq.heapify(queue)

        while len(seen) < len(workers):

            _, worker, bike = heapq.heappop(queue)

            if bike not in seen:
                seen.add(bike)
                ans[worker] = bike

            else:
                heapq.heappush(queue, distances[worker].pop())

        return ans

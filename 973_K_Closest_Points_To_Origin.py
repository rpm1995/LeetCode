import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def distance(point1, point2):

            x1 = point1[0]
            x2 = point2[0]
            y1 = point1[1]
            y2 = point2[1]

            return ((x2 - x1) ** 2 + (y2 - y1) ** 2)

        ans = []
        heap = []
        heapq.heapify(heap)

        for point in points:

            to_add = (-distance([0, 0], point), point)

            if len(heap) == K:
                heapq.heappushpop(heap, to_add)
            else:
                heapq.heappush(heap, to_add)

        while heap:
            distance, point = heapq.heappop(heap)
            ans.append(point)

        return ans

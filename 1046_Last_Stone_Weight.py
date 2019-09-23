import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []
        heapq.heapify(heap)

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:

            first_stone = abs(heapq.heappop(heap))
            second_stone = abs(heapq.heappop(heap))

            if first_stone == second_stone:
                continue

            heapq.heappush(heap, -(abs(first_stone - second_stone)))

        if not heap:
            return 0
        return -heapq.heappop(heap)

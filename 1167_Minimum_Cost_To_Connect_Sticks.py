import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        cost = 0
        heap = []
        heapq.heapify(heap)

        for stick in sticks:
            heapq.heappush(heap, stick)

        while len(heap) > 1:
            stick1 = heapq.heappop(heap)
            stick2 = heapq.heappop(heap)

            new_stick = stick1 + stick2
            cost += new_stick

            heapq.heappush(heap, new_stick)

        return cost

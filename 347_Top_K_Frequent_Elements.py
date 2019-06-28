import heapq


class Solution(object):
    def topKFrequent(self, nums, k):

        heap = []
        heapq.heapify(heap)
        freqs = {}
        ans = []

        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1

        for value, frequency in freqs.items():

            if len(heap) >= k:
                heapq.heappushpop(heap, (frequency, value))
            else:
                heapq.heappush(heap, (frequency, value))

        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans

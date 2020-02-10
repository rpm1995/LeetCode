import heapq


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        heap = []
        heapq.heapify(heap)

        for index, element in enumerate(nums[:-1]):
            second = nums[index + 1]
            distance = abs(second - element)

            heapq.heappush(heap, (distance, index, index + 1))

        for _ in range(k):

            distance, index_1, index_2 = heapq.heappop(heap)

            if index_2 < len(nums) - 1:
                new_distance = abs(nums[index_2 + 1] - nums[index_1])
                heapq.heappush(heap, (new_distance, index_1, index_2 + 1))

        return distance

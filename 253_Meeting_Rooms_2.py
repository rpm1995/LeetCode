import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        ans = 1
        count = 1
        intervals.sort()
        heap = [intervals[0][1]]
        heapq.heapify(heap)

        for start, end in intervals[1:]:

            if start < heap[0]:
                heapq.heappush(heap, end)
                ans += 1
            elif start >= heap[0]:
                heapq.heappushpop(heap, end)  # Just need to pop out ONE room, put the meeting in there!

        return ans

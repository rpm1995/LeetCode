# from collections import deque
#
#
# class HitCounter:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.queue = deque([])
#
#     def hit(self, timestamp: int) -> None:
#         """
#         Record a hit.
#         @param timestamp - The current timestamp (in seconds granularity).
#         """
#         self.queue.append(timestamp)
#
#     def getHits(self, timestamp: int) -> int:
#         """
#         Return the number of hits in the past 5 minutes.
#         @param timestamp - The current timestamp (in seconds granularity).
#         """
#         while self.queue and timestamp - self.queue[0] >= 300:
#             self.queue.popleft()
#
#         return len(self.queue)
#
# # Your HitCounter object will be instantiated and called as such:
# # obj = HitCounter()
# # obj.hit(timestamp)
# # param_2 = obj.getHits(timestamp)

# O(300) getHits()

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = [[i + 1, 0] for i in range(300)]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        index = (timestamp - 1) % 300

        if self.counter[index][0] == timestamp:
            self.counter[index][1] += 1

        else:  # Greater than 300s
            self.counter[index][0] = timestamp
            self.counter[index][1] = 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        ans = 0

        for t, freq in self.counter:

            if timestamp - t < 300:
                ans += freq

        return ans

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

import heapq


class Leaderboard:

    def __init__(self):

        self.players = {}

    def addScore(self, playerId: int, score: int) -> None:

        if playerId not in self.players:
            self.players[playerId] = 0
        self.players[playerId] += score

    def top(self, K: int) -> int:

        ans = 0
        heap = []
        heapq.heapify(heap)

        for key, val in self.players.items():
            heapq.heappush(heap, val)

            if len(heap) > K:
                heapq.heappop(heap)

        for score in heap:
            ans += score

        return ans

    def reset(self, playerId: int) -> None:

        del self.players[playerId]

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

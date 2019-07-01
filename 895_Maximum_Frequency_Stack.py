import heapq


class FreqStack:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.index = 0
        self.freqs = {}

    def push(self, x: int) -> None:
        self.index += 1

        if x not in self.freqs:
            self.freqs[x] = 0
        self.freqs[x] += 1

        frequency = self.freqs[x]
        self.index += 1

        heapq.heappush(self.heap, (-frequency, -self.index, x))

    def pop(self) -> int:
        frequency, index, value = heapq.heappop(self.heap)
        self.freqs[value] -= 1
        return value

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

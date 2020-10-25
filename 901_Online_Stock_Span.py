class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        result = 1

        while self.stack and price >= self.stack[-1][0]:
            result += self.stack.pop()[1]

        self.stack.append((price, result))

        return result

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

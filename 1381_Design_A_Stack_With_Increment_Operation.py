class CustomStack:

    def __init__(self, maxSize: int):

        self.stack = []
        self.size = maxSize
        self.increments = [0 for _ in range(self.size)]

    def push(self, x: int) -> None:

        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self) -> int:

        if not self.stack:
            return -1

        index = len(self.stack) - 1
        ret_me = self.stack.pop() + self.increments[index]

        if self.stack:
            self.increments[index - 1] += self.increments[index]
        self.increments[index] = 0

        return ret_me

    def increment(self, k: int, val: int) -> None:

        if self.stack:
            self.increments[min(k, len(self.stack)) - 1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

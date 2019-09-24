class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_ = -float('inf')

    def push(self, x: int) -> None:

        max_ = x

        if self.stack:
            max_ = max(max_, self.stack[-1][1])

        self.stack.append((x, max_))

    def pop(self) -> int:

        number, max_ = self.stack.pop()

        return number

    def top(self) -> int:

        return self.stack[-1][0]

    def peekMax(self) -> int:

        return self.stack[-1][1]

    def popMax(self) -> int:

        second_stack = []
        max_ = self.stack[-1][1]

        while self.stack[-1][0] != max_:
            second_stack.append(self.stack.pop())

        retme, next_max = self.stack.pop()

        while second_stack:
            element, _ = second_stack.pop()
            self.push(element)

        return retme

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
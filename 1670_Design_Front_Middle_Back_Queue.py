from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):

        self.front = deque([])
        self.back = deque([])

    def pushFront(self, val: int) -> None:

        self.front.appendleft(val)

        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())

    def pushMiddle(self, val: int) -> None:

        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())

        self.front.append(val)

    def pushBack(self, val: int) -> None:

        self.back.append(val)

        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())

    def popFront(self) -> int:

        if not self.front and not self.back:
            return -1

        retme = self.front.popleft()

        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())

        return retme

    def popMiddle(self) -> int:

        if not self.front and not self.back:
            return -1

        retme = self.front.pop()

        if len(self.front) < len(self.back):
            self.front.append(self.back.popleft())

        return retme

    def popBack(self) -> int:

        if not self.front and not self.back:
            return -1

        if not self.back:
            return self.front.pop()

        retme = self.back.pop()

        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())

        return retme

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

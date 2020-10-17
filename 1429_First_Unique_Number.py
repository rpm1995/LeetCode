from collections import deque


class FirstUnique:

    def __init__(self, nums: List[int]):

        self.queue = deque([])
        self.is_unique = {}

        for num in nums:

            if num not in self.is_unique:
                self.queue.append(num)
                self.is_unique[num] = True

            else:
                self.is_unique[num] = False

    def showFirstUnique(self) -> int:

        while self.queue and self.is_unique[self.queue[0]] is False:
            self.queue.popleft()

        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:

        if value not in self.is_unique:
            self.queue.append(value)
            self.is_unique[value] = True

        else:
            self.is_unique[value] = False

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

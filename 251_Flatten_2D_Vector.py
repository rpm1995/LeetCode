class Vector2D:

    def __init__(self, v: List[List[int]]):

        self.holdme = []
        self.pointer = 0

        for inner_list in v:
            for inner_values in inner_list:
                self.holdme.append(inner_values)

    def next(self) -> int:

        ans = self.holdme[self.pointer]
        self.pointer += 1
        return ans

    def hasNext(self) -> bool:

        if self.pointer < len(self.holdme):
            return True
        return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

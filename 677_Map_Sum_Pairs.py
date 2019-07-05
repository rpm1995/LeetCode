class node:
    def __init__(self):
        self.children = {}
        self.value = 0


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = node()

    def insert(self, key: str, val: int) -> None:

        pointer = self.root

        for char in key:
            if char not in pointer.children:
                pointer.children[char] = node()
            pointer = pointer.children[char]

        pointer.value = val

    def sum(self, prefix: str) -> int:

        pointer = self.root
        ans = 0

        for char in prefix:
            if char not in pointer.children:
                return 0
            pointer = pointer.children[char]

        stack = [pointer]

        while stack:
            cur_node = stack.pop()
            ans += cur_node.value

            stack.extend(cur_node.children.values())

        return ans

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

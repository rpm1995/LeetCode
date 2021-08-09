class Solution:

    def get_invalid_index(self, s):

        characters = {}

        for char in s:
            if char not in characters:
                characters[char] = 0
            characters[char] += 1

        for index, char in enumerate(s):
            if characters[char] < self.k:
                return index

        return len(s)

    def solve(self, s):

        index = self.get_invalid_index(s)

        if index == len(s):
            self.ans = max(self.ans, len(s))
            return

        self.solve(s[: index])
        self.solve(s[index + 1:])

    def longestSubstring(self, s: str, k: int) -> int:

        self.k = k
        self.ans = 0
        self.solve(s)

        return self.ans

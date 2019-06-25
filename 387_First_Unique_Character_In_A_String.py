class Solution:
    def firstUniqChar(self, s: str) -> int:

        dicti = {}

        for char in s:
            if char not in dicti:
                dicti[char] = 0
            dicti[char] += 1

        for index, char in enumerate(s):
            if dicti[char] == 1:
                return index

        return -1

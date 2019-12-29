class Solution:
    def titleToNumber(self, s: str) -> int:
        def get_number(char):
            return (ord(char) - ord('A')) + 1

        ans = 0

        for char in s:
            ans = (ans * 26) + get_number(char)

        return ans

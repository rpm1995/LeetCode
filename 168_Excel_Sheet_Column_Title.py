class Solution:
    def convertToTitle(self, n: int) -> str:
        def get_char(r):
            char = chr(r + ord("A"))
            return char

        ans = ""

        while n > 0:
            n -= 1
            remainder = n % 26
            ans += get_char(remainder)
            n //= 26

        return ''.join(reversed(ans))

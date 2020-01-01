class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palin(string):

            return string == string[::-1]

        start = 0
        end = len(s) - 1

        while start < end:

            if s[start] == s[end]:
                start += 1
                end -= 1

            else:
                return check_palin(s[start + 1: end + 1]) or check_palin(s[start: end])

        return True

class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ans = ""
        max_length = 0

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1):
            dp[i][i + 1] = 1 if s[i] == s[i + 1] else 0

        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and dp[i + 1][j - 1] is 1:
                    dp[i][j] = 1

        for i in range(n):
            for j in range(i, n):
                if dp[i][j] == 1:
                    if j - i + 1 > max_length:
                        ans = s[i:j + 1]
                        max_length = j - i + 1

        return ans

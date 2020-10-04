class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key=lambda x: len(x))
        dp = {}
        ans = 0

        for word in words:
            dp[word] = 1

        for word in words:

            for i in range(len(word)):
                split = word[:i] + word[i + 1:]

                if split in dp:
                    dp[word] = max(dp[word], dp[split] + 1)

            ans = max(ans, dp[word])

        return ans

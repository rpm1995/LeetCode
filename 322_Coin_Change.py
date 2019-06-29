class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for current in range(coin, len(dp)):

                if dp[current - coin] != -1:
                    if dp[current] == -1:
                        dp[current] = dp[current - coin] + 1
                    else:
                        dp[current] = min(dp[current], dp[current - coin] + 1)

        print(dp)
        return dp[-1]

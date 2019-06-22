class Solution:
    def bulbSwitch(self, n: int) -> int:
        #         if n == 1:
        #             return 1

        #         bulbs = [False for _ in range(n)]

        #         for i in range(1, n+1):
        #             for bulb in range(i, n+1, i):

        #                 bulbs[bulb-1] = bulbs[bulb-1] ^ True

        #         ans = 0

        #         for bulb in bulbs:
        #             if bulb is True:
        #                 ans += 1

        #         return ans

        return int(n ** 0.5)

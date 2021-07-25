class Solution:
    def trailingZeroes(self, n: int) -> int:

        ans = 0

        for i in range(1, n + 1):

            if i % 5 == 0:

                multiple_5 = i

                while multiple_5 % 5 == 0:
                    ans += 1
                    multiple_5 //= 5

        return ans

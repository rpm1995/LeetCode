class Solution:
    def countPrimes(self, n: int) -> int:

        nums = [i for i in range(n)]
        ans = 0

        for i in range(2, n // 2 + 1):          # Can improve this

            j = i * 2

            while j < n:

                if nums[j] > 0:
                    nums[j] *= -1
                j += i

        for i in range(2, n):
            if nums[i] > 0:
                ans += 1

        return ans

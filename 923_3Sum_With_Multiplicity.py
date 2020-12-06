class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:

        ans = 0
        mod = 10 ** 9 + 7
        A.sort()

        for i, value in enumerate(A):

            to_find = target - value
            j = i + 1
            k = len(A) - 1

            while j < k:

                if A[j] + A[k] < to_find:
                    j += 1

                elif A[j] + A[k] > to_find:
                    k -= 1

                elif A[j] != A[k]:

                    left = 1
                    while j + 1 < k and A[j] == A[j + 1]:
                        left += 1
                        j += 1

                    right = 1
                    while k - 1 > j and A[k] == A[k - 1]:
                        right += 1
                        k -= 1

                    ans += left * right
                    ans %= mod

                    j += 1
                    k -= 1

                else:

                    n = k - j + 1
                    ans += (n * (n - 1)) / 2
                    ans %= mod

                    break

        return int(ans)

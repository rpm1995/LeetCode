class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        n = len(A)
        ans = [0 for _ in range(n)]
        start = 0
        end = n - 1

        for integer in A:

            if integer % 2 == 0:
                ans[start] = integer
                start += 1

            else:
                ans[end] = integer
                end -= 1

        return ans

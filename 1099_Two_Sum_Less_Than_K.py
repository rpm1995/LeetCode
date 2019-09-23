class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:

        ans = -1
        A.sort()
        left = 0
        right = len(A) - 1

        while left < right:

            sum_ = A[left] + A[right]

            if sum_ < K:
                left += 1
                ans = max(ans, sum_)

            else:
                right -= 1

        return ans

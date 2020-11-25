class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        left = 0
        ans = 0
        count = 0

        for right, value in enumerate(A):

            if value == 0:
                count += 1

            while left <= right and count > K:

                left_val = A[left]

                if left_val == 0:
                    count -= 1

                left += 1

            ans = max(ans, right - left + 1)

        return ans

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        start = 0
        end = n - k - 1
        subarray_sum = sum(cardPoints[: end + 1])
        min_subarray_sum = subarray_sum

        while end < n - 1:
            end += 1
            subarray_sum = subarray_sum - cardPoints[start] + cardPoints[end]
            min_subarray_sum = min(min_subarray_sum, subarray_sum)
            start += 1

        return sum(cardPoints) - min_subarray_sum

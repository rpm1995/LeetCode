class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        buckets = [0 for _ in range(10001)]

        for num in nums:
            buckets[num] += num

        skip = [0 for _ in range(10001)]
        take = [0 for _ in range(10001)]

        for i in range(len(buckets)):
            take[i] = skip[i - 1] + buckets[i]
            skip[i] = max(skip[i - 1], take[i - 1])

        return max(take[-1], skip[-1])

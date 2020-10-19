from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        min_queue = deque()
        max_queue = deque()
        start = 0
        end = 0
        ans = 0

        while end < len(nums):

            while min_queue and nums[min_queue[-1]] >= nums[end]:
                min_queue.pop()

            while max_queue and nums[max_queue[-1]] <= nums[end]:
                max_queue.pop()

            min_queue.append(end)
            max_queue.append(end)

            while nums[max_queue[0]] - nums[min_queue[0]] > limit:

                start += 1

                if max_queue[0] < start:
                    max_queue.popleft()

                if min_queue[0] < start:
                    min_queue.popleft()

            ans = max(ans, end - start + 1)

            end += 1

        return ans

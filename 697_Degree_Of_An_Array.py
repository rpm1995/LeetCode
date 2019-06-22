class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0

        degree = 0
        freqs = {}

        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1

        for key, value in freqs.items():
            if value > degree:
                degree = value

        left = 0
        right = 0
        freqs_window = {}
        degree_window = 0
        ans = float('inf')

        while right < len(nums):

            new_number = nums[right]
            if new_number not in freqs_window:
                freqs_window[new_number] = 0
            freqs_window[new_number] += 1

            if freqs_window[new_number] == degree:

                ans = min(ans, right - left + 1)
                degree_window = degree

                while left < right and degree_window == degree:
                    ans = min(ans, right - left + 1)
                    freqs_window[nums[left]] -= 1
                    left += 1
                    degree_window = 0

                    for key, value in freqs_window.items():
                        if value > degree_window:
                            degree_window = value

            right += 1

        return ans if ans != float('inf') else 1

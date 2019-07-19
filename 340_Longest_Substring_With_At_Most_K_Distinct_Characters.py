class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        window_dict = {}
        ans = 0
        left = 0
        right = 0

        while right < len(s):

            current = s[right]

            if current not in window_dict:
                window_dict[current] = 0
            window_dict[current] += 1

            while len(window_dict) > k:

                previous = s[left]
                window_dict[previous] -= 1

                if window_dict[previous] == 0:
                    del window_dict[previous]

                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans

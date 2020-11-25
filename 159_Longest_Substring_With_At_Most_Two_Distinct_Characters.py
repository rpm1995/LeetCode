class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        counts = {}
        left = 0
        ans = 0

        for right, right_char in enumerate(s):

            if right_char not in counts:
                counts[right_char] = 0
            counts[right_char] += 1

            while left < right and len(counts) > 2:

                left_char = s[left]
                counts[left_char] -= 1

                if counts[left_char] == 0:
                    del counts[left_char]

                left += 1

            ans = max(ans, right - left + 1)

        return ans

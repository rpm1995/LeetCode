class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        window_dict = {}
        left = 0
        right = 0

        if not s:
            return 0

        while right < len(s):

            current_char = s[right]

            #             if current_char not in window_dict:
            #                 window_dict[current_char] = right
            #                 # ans += 1

            #             else:
            #                 left = window_dict[current_char] + 1
            #                 window_dict[current_char] = right

            if current_char in window_dict and window_dict[current_char] >= left:
                left = window_dict[current_char] + 1

            else:
                ans = max(ans, right - left + 1)

            window_dict[current_char] = right
            right += 1

            # print(ans)

        return ans

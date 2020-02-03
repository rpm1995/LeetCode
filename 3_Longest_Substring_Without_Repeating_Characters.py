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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        end = 0
        chars_in_substring = set()
        longest_length = 0
        n = len(s)

        while end < n:

            new_char = s[end]

            while start < end and new_char in chars_in_substring:
                old_char = s[start]
                chars_in_substring.remove(old_char)
                start += 1

            chars_in_substring.add(new_char)
            longest_length = max(longest_length, end - start + 1)
            end += 1

        return longest_length


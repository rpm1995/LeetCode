class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s_dict = {}
        t_dict = {}
        s_unique = 0
        t_unique = 0
        left = 0
        right = 0
        ans = ""

        for char in t:
            if char not in t_dict:
                t_dict[char] = 0
                t_unique += 1
            t_dict[char] += 1

        while right < len(s):

            new_char = s[right]

            if new_char in t_dict:

                if new_char not in s_dict:
                    s_dict[new_char] = 0
                s_dict[new_char] += 1

                if s_dict[new_char] == t_dict[new_char]:
                    s_unique += 1

                while left <= right and s_unique >= t_unique:
                    ans = s[left:right + 1] if len(ans) > right - left + 1 or ans == "" else ans

                    old_char = s[left]

                    if old_char in s_dict:
                        s_dict[old_char] -= 1

                        if s_dict[old_char] < t_dict[old_char]:
                            s_unique -= 1

                    left += 1

            right += 1

        return ans

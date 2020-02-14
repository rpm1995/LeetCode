class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s_dict = {}
        t_dict = {}
        similarity = 0
        left = 0
        right = 0
        ans = ""
        min_length = float('inf')

        for char in t:
            if char not in t_dict:
                t_dict[char] = 0
            t_dict[char] += 1

        while right < len(s):
            char = s[right]

            if char in t_dict:
                if char not in s_dict:
                    s_dict[char] = 0
                s_dict[char] += 1

                if s_dict[char] == t_dict[char]:
                    similarity += 1

                while similarity == len(t_dict):
                    if right - left + 1 < min_length:
                        min_length = right - left + 1
                        ans = s[left: right + 1]

                    left_char = s[left]

                    if left_char in t_dict:
                        s_dict[left_char] -= 1

                        if s_dict[left_char] < t_dict[left_char]:
                            similarity -= 1

                    left += 1
            right += 1

        return ans

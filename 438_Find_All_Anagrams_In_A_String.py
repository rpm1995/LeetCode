class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_len = len(p)
        p_map = [0 for _ in range(26)]
        s_map = [0 for _ in range(26)]
        ans = []

        for char in p:
            index = ord(char) - ord('a')
            p_map[index] += 1

        for cur_index, char in enumerate(s):

            char_index = ord(char) - ord('a')
            s_map[char_index] += 1

            if cur_index >= p_len:
                s_map[ord(s[cur_index - p_len]) - ord('a')] -= 1

            if s_map == p_map:
                ans.append(cur_index - p_len + 1)

        return ans

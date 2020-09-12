class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        def helper(s_index, t_index):

            if s_index == len_s:
                return True
            if t_index == len_t:
                return False

            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

            return helper(s_index, t_index)

        len_s = len(s)
        len_t = len(t)

        return helper(0, 0)

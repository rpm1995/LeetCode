class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        ans = ""
        running_count = 0

        start = 0
        end = 0

        while end < len(S):

            if S[end] == "(":
                running_count += 1

            else:
                running_count -= 1

            if running_count == 0:
                ans += S[start + 1: end]
                start = end + 1

            end += 1

        return ans

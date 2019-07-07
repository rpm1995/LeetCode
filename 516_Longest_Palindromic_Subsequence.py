class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        #         def helper(word, start, end):

        #             if start == end:
        #                 return 1

        #             if start > end:
        #                 return 0

        #             if word[start] == word[end]:
        #                 return 2 + helper(word, start+1, end-1)
        #             else:
        #                 return max(helper(word, start+1, end), helper(word, start, end-1))

        #         n = len(s)
        #         return helper(s, 0, n-1)

        def helper(word, left, right):

            if left == right:
                return 1

            if left > right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            if word[left] == word[right]:
                memo[(left, right)] = 2 + helper(word, left + 1, right - 1)

            else:
                memo[(left, right)] = max(helper(word, left + 1, right), helper(word, left, right - 1))

            return memo[(left, right)]

        memo = {}
        n = len(s)
        return helper(s, 0, n - 1)

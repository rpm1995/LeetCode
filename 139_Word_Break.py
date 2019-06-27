class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        #         def helper(start):

        #             if start == len(s):
        #                 return True

        #             for i in range(start, len(s)+1):

        #                 if s[start:i] in words:
        #                     if helper(i) is True:
        #                         return True

        #             return False

        #         words = set(wordDict)
        #         return helper(0)

        def helper(start, visited):

            if start in visited:
                return visited[start]

            if start == len(s):
                return True

            visited[start] = False

            for i in range(start, len(s) + 1):

                if s[start: i] in words:
                    if helper(i, visited) is True:
                        visited[i] = True  # May or may not add this
                        visited[start] = True
                        return True

            return False

        words = set(wordDict)
        return helper(0, {})

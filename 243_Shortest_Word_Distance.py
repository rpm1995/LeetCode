class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:

        index1 = -1
        index2 = -1
        ans = float('inf')

        for index, word in enumerate(words):

            if word == word1:
                index1 = index

                if index2 != -1:
                    ans = min(ans, abs(index1 - index2))

            if word == word2:
                index2 = index

                if index1 != -1:
                    ans = min(ans, abs(index1 - index2))

        return ans

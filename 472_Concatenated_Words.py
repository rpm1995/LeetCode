class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        def helper(word):

            if not word:
                return True

            for i in range(1, len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in wordset:
                    if suffix in wordset:
                        return True
                    if helper(suffix):
                        return True

            return False

        wordset = set(words)
        ans = []

        for word in words:
            if word:  # Special Test Case
                wordset.remove(word)
                if helper(word) is True:
                    ans.append(word)
                wordset.add(word)

        return ans

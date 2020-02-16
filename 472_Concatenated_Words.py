class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words_set = set(words)
        ans = []

        def is_concatenated(word, start, words_set, cache):
            if start >= len(word):
                return True

            if cache[start] is not None:
                return cache[start]

            for end in range(start, len(word) + 1):
                if word[start: end + 1] in words_set:
                    if is_concatenated(word, end + 1, words_set, cache):
                        cache[start] = True
                        return cache[start]

            cache[start] = False
            return cache[start]

        for word in words:
            if word:  # Silly test case
                words_set.remove(
                    word)  # We do this because we do not want the smaller words itself to be part of the answer

                if is_concatenated(word, 0, words_set, [None for _ in range(len(word))]):
                    ans.append(word)

                words_set.add(word)

        return ans

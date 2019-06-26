class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        for c in "!?',;.": paragraph = paragraph.replace(c, " ")

        counts = {}
        banned = set(banned)
        maxcount = 0
        maxword = ""

        for word in paragraph.split():
            word = word.lower()

            if word in banned:
                continue

            if word not in counts:
                counts[word] = 0
            counts[word] += 1

            if counts[word] > maxcount:
                maxcount = counts[word]
                maxword = word

        return maxword

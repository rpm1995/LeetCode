class Solution:
    def toGoatLatin(self, S: str) -> str:

        ans = []
        count = 0

        for word in S.split(" "):

            count += 1

            if word[0] not in "aeiouAEIOU":
                word = word[1:] + word[0:1]

            word += "ma"
            word += "a" * count

            ans.append(word)

        return ' '.join(ans)

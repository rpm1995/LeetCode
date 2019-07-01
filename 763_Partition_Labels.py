class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        last_indices = [0 for _ in range(26)]

        for index, letter in enumerate(S):
            ascii_ = ord(letter) - ord('a')
            last_indices[ascii_] = index

        start = 0
        highestsofar = 0
        ans = []

        for index, letter in enumerate(S):

            ascii_ = ord(letter) - ord('a')
            highestsofar = max(last_indices[ascii_], highestsofar)

            if highestsofar == index:
                ans.append(highestsofar - start + 1)
                start = index + 1

        return ans

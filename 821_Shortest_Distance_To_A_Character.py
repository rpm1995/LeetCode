class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:

        #         def getClosestIndex(index, char_index):

        #             distance = float('inf')

        #             for i, candidate_index in enumerate(char_index):

        #                 if abs(candidate_index-index) < distance:
        #                     distance = abs(candidate_index - index)

        #             return distance

        #         ans = []
        #         char_index = []

        #         for index, c in enumerate(S):
        #             if c == C:
        #                 char_index.append(index)

        #         for index, s in enumerate(S):

        #             if s == C:
        #                 ans.append(0)
        #             else:
        #                 ans.append(getClosestIndex(index, char_index))

        #         return ans

        closest = []
        ans = []

        prev = -float('inf')
        for index, char in enumerate(S):

            if char == C:
                prev = index
            closest.append(index - prev)

        prev = float('inf')
        for index in range(len(S) - 1, -1, -1):

            if S[index] == C:
                prev = index
            ans.append(min(closest[index], prev - index))

        return reversed(ans)

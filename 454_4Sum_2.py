class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        dicti = {}
        ans = 0

        for a in A:
            for b in B:

                if a + b not in dicti:
                    dicti[a + b] = 0
                dicti[a + b] += 1

        for c in C:
            for d in D:

                if 0 - (c + d) in dicti:
                    ans += dicti[0 - (c + d)]

        return ans

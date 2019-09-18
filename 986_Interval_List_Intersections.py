class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        res = []
        idxA = 0
        idxB = 0

        while idxA < len(A) and idxB < len(B):

            lower = max(A[idxA][0], B[idxB][0])
            higher = min(A[idxA][1], B[idxB][1])

            if lower <= higher:
                res.append([lower, higher])

            if A[idxA][1] <= B[idxB][1]:
                idxA += 1
            else:
                idxB += 1

        return res

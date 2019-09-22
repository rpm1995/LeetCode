class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        negative = 0
        positive = 0
        n = len(A)
        ans = []

        while positive < n and A[positive] < 0:
            positive += 1
        negative = positive - 1

        while negative >= 0 and positive < n:

            if abs(A[negative]) <= abs(A[positive]):
                ans.append(A[negative] ** 2)
                negative -= 1
            else:
                ans.append(A[positive] ** 2)
                positive += 1

        while positive < n:
            ans.append(A[positive] ** 2)
            positive += 1

        while negative >= 0:
            ans.append(A[negative] ** 2)
            negative -= 1

        return ans

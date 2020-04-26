class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:

        ans = ""

        for i, h1 in enumerate(A):
            for j, h2 in enumerate(A):
                for k, m1 in enumerate(A):
                    for l, m2 in enumerate(A):

                        if i != j and j != k and k != l and i != k and i != l and j != l:
                            time = str(h1) + str(h2) + ":" + str(m1) + str(m2)

                            if str(h1) + str(h2) < "24" and str(m1) + str(m2) < "60":
                                ans = max(ans, time)

        return ans

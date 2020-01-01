class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        increasing = True
        for index, value in enumerate(A):

            if index > 0:

                if value < A[index - 1] and increasing is True:
                    return index - 1

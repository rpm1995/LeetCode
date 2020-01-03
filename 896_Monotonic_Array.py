class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        def check_all_equal(arr):

            value = arr[0]

            for element in arr:
                if element != value:
                    return False

            return True

        if A[0] == A[-1]:
            return check_all_equal(A)

        increasing = True

        if A[0] > A[-1]:
            increasing = False

        for index in range(1, len(A)):

            if A[index] > A[index - 1] and not increasing:
                return False

            if A[index] < A[index - 1] and increasing:
                return False

        return True

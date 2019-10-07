class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        zeroes = 0
        n = len(arr)

        for num in arr:
            if num == 0:
                zeroes += 1

        for index in range(n - 1, -1, -1):

            if index + zeroes < n:
                arr[index + zeroes] = arr[index]

            if arr[index] == 0:
                zeroes -= 1

                if index + zeroes < n:
                    arr[index + zeroes] = arr[index]

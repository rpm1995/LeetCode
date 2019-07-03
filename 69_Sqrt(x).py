class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1:
            return 1
        if x == 0:
            return 0

        left = 1
        right = x

        while left <= right:

            mid = (left + right) // 2

            if mid ** 2 == x:
                return mid

            if mid ** 2 > x:
                right = mid - 1

            else:
                left = mid + 1

        return right

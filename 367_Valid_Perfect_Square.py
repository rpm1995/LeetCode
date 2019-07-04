class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left = 1
        right = num

        if num == 1:
            return True

        if num == 0:
            return False

        while left <= right:

            mid = (left + right) // 2

            if mid * mid == num:
                return True

            elif mid * mid < num:
                left = mid + 1

            else:
                right = mid - 1

        return False

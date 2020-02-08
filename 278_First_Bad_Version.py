# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n

        while left < right:

            mid = (left + right) // 2
            is_bad = isBadVersion(mid)

            if not is_bad:
                left = mid + 1

            else:
                right = mid

        return right

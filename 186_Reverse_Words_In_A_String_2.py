class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(start, end):

            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        reverse(0, len(s) - 1)
        left = 0
        right = 0

        while right < len(s):

            while right < len(s) and s[right].isspace() is False:
                right += 1
            reverse(left, right - 1)

            right += 1
            left = right

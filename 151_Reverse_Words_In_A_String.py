class Solution:
    def reverseWords(self, s: str) -> str:

        def reverse_string(start, end, string):

            while start < end:
                string[start], string[end] = string[end], string[start]
                start += 1
                end -= 1

        def reverse_words(string):

            left, right = 0, 0

            while right < n:

                while right < n and string[right].isspace() is False:
                    right += 1

                reverse_string(left, right - 1, string)
                right += 1
                left = right

        def strip(string):

            if ''.join(string).isspace():  # Check for silly test case
                return []

            left = 0
            right = n - 1

            while left < right and string[left].isspace():
                left += 1

            while right > left and string[right].isspace():
                right -= 1

            return string[left:right + 1]

        def remove_spaces(string):

            left, right = 0, 0
            retme = []

            while right < len(string):

                while right < len(string) and string[right].isspace() is False:
                    right += 1

                retme.extend(string[left:right + 1])

                while right < len(string) and string[right].isspace():
                    right += 1

                left = right

            return retme

        ans = list(s)
        n = len(s)
        reverse_string(0, n - 1, ans)
        reverse_words(ans)
        ans = strip(ans)
        ans = remove_spaces(ans)

        return ''.join(ans)

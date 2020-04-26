class Solution:
    def compress(self, chars: List[str]) -> int:

        write_here = 0
        start = 0

        while start < len(chars):

            end = start + 1

            while end < len(chars) and chars[end] == chars[start]:
                end += 1

            chars[write_here] = chars[start]
            write_here += 1

            if end - start > 1:
                for digit in str(end - start):
                    chars[write_here] = digit
                    write_here += 1

            start = end

        final_length = write_here
        return final_length

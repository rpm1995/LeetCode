class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Number of characters to change to turn string into one character = length of string - frequency of most common char

        freqs = [0 for _ in range(26)]
        start = 0
        max_freq = 0
        ans = 0

        for end, char in enumerate(s):

            char_loc = ord(char) - ord('A')
            freqs[char_loc] += 1
            max_freq = max(max_freq, freqs[char_loc])

            if end - start + 1 - max_freq > k:
                start_char = s[start]
                start_char_loc = ord(start_char) - ord('A')
                freqs[start_char_loc] -= 1

                start += 1

            ans = max(ans, end - start + 1)

        return ans

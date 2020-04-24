class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def get_xor(string):
            xor_value = 0

            for char in string:
                xor_value ^= ord(char)

            return xor_value

        s_xor = get_xor(s)
        t_xor = get_xor(t)

        return chr(s_xor ^ t_xor)

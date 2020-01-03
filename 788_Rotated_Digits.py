class Solution:
    def rotatedDigits(self, N: int) -> int:

        dont_rotate = "347"
        rotation = {"0": "0",
                    "1": "1",
                    "8": "8",
                    "2": "5",
                    "5": "2",
                    "6": "9",
                    "9": "6"}

        def is_not_good(n):

            n = str(n)

            for digit in n:
                if digit in dont_rotate:
                    return True

            return False

        def is_same_after_rotation(n):

            n = str(n)
            new_number = ""

            for digit in n:
                new_number += rotation[digit]

            return new_number == n

        ans = 0

        for number in range(1, N + 1):
            if not is_not_good(number) and not is_same_after_rotation(number):
                ans += 1

        return ans

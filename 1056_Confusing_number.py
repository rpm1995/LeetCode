class Solution:
    def confusingNumber(self, N: int) -> bool:

        invalid = set([2, 3, 4, 5, 7])
        valid = {0: 0,
                 1: 1,
                 8: 8,
                 6: 9,
                 9: 6}
        old_number = N
        new_number = 0

        while N:

            last_digit = N % 10

            if last_digit in invalid:
                return False

            new_number = new_number * 10 + valid[last_digit]
            N //= 10

        return new_number != old_number

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = False

        if divisor < 0 or dividend < 0:
            if divisor < 0 and dividend < 0:
                negative = False
            else:
                negative = True

        divisor = abs(divisor)
        dividend = abs(dividend)
        quotient = 0

        #         while dividend >= divisor:

        #             quotient += 1
        #             dividend -= divisor

        while dividend >= divisor:

            power_two = 1
            value = divisor

            while value + value <= dividend:
                # print(value, dividend)
                value += value
                power_two += power_two

            quotient += power_two
            dividend -= value

        return quotient if not negative else -quotient

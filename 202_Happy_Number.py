class Solution:
    def isHappy(self, n: int) -> bool:

        def calculate(number):

            sum_ = 0

            while number:
                digit = number % 10
                sum_ += (digit * digit)
                number //= 10

            return sum_

        seen_sums = set()

        while True:

            number = calculate(n)

            if number in seen_sums:
                return False

            if number == 1:
                return True

            seen_sums.add(number)
            n = number

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_ = 0

        while n:
            digit = n % 10
            product *= digit
            sum_ += digit
            n //= 10

        return product - sum_

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = False

        for index in range(len(digits) - 1, -1, -1):

            digit = digits[index]

            if digit == 9:
                digits[index] = 0
                carry = True

            else:
                digits[index] += 1
                carry = False
                break

        if carry:
            digits.insert(0, 1)

        return digits

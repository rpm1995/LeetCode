class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = ""
        carry = 0
        index = 0

        while index < min(len(num1), len(num2)):

            digit1 = int(num1[index])
            digit2 = int(num2[index])

            sum_ = digit1 + digit2 + carry

            if sum_ >= 10:
                sum_ = sum_ % 10
                carry = 1
            else:
                carry = 0

            ans += str(sum_)
            index += 1

        if index == len(num1) and index == len(num2):
            if carry == 1:
                ans += "1"
            return ans[::-1]

        elif index == len(num1):
            while index < len(num2):

                sum_ = int(num2[index]) + carry

                if sum_ >= 10:
                    sum_ = sum_ % 10
                    carry = 1
                else:
                    carry = 0
                ans += str(sum_)
                index += 1

        else:
            while index < len(num1):
                sum_ = int(num1[index]) + carry

                if sum_ >= 10:
                    sum_ = sum_ % 10
                    carry = 1
                else:
                    carry = 0
                ans += str(sum_)
                index += 1

        if carry == 1:
            ans += "1"
        return ans[::-1]

# class Solution:
#     def intToRoman(self, num: int) -> str:
#
#         romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#         values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#         ans = ""
#
#         pointer = 0
#
#         while num > 0:
#
#             if num - values[pointer] >= 0:
#                 ans += romans[pointer]
#                 num -= values[pointer]
#             else:
#                 pointer += 1
#
#         return ans

class Solution:
    def intToRoman(self, num: int) -> str:

        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ""

        pointer = 0

        while num > 0:

            # if num - values[pointer] >= 0:
            #     ans += romans[pointer]
            #     num -= values[pointer]
            # else:
            #     pointer += 1

            times = num // values[pointer]

            if times > 0:

                ans = ans + (times * romans[pointer])
                num %= values[pointer]

            else:
                pointer += 1

        return ans


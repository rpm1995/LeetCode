class Solution:
    def myAtoi(self, string: str) -> int:

        string = string.strip()
        ans = 0
        sign = "+"
        index = 0

        if not string:
            return 0

        if string[0] != "+" and string[0] != "-" and string[0].isdigit() is False:
            return 0

        if string[0] == "-":
            sign = "-"
            index += 1
        elif string[0] == "+":
            index += 1

        while index < len(string):

            if string[index].isdigit() is False:
                ans = ans if sign == "+" else - ans

                if ans < -2 ** 31:
                    return -2 ** 31
                elif ans > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                else:
                    return ans

            ans = 10 * ans + int(string[index])
            index += 1

        ans = ans if sign == "+" else -ans

        if ans < -2 ** 31:
            return -2 ** 31
        elif ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return ans

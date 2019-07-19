class Solution:
    def calculate(self, s: str) -> int:

        s = s.strip()
        num = 0
        stack = []
        operators = "+-/*"
        sign = "+"
        ans = 0

        for index, token in enumerate(s):

            if token not in operators and token.isdigit() is False:
                continue

            if token.isdigit() is True:
                num = num * 10 + int(token)

            if token in operators or index == len(s) - 1:

                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(num * stack.pop())
                elif sign == "/":
                    stack.append(int(float(stack.pop()) / num))

                sign = token
                num = 0

            # print(stack)

        for leftovers in stack:
            ans += leftovers

        return ans

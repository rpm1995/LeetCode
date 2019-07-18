class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        signs = "+-*/"

        for item in tokens:

            if item in signs:
                operand1 = stack.pop()
                operand2 = stack.pop()

                if item == "+":
                    stack.append(operand1 + operand2)

                elif item == "-":
                    stack.append(operand2 - operand1)

                elif item == "*":
                    stack.append(operand1 * operand2)

                else:
                    stack.append(int(float(operand2) / operand1))  # Takes care of 1/-22 cases

            else:
                stack.append(int(item))

        return stack.pop()

class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {")": "(",
                   "]": "[",
                   "}": "{"}
        open_brackets = set(["(", "[", "{"])

        stack = []

        for bracket in s:

            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if not stack or stack[-1] != mapping[bracket]:
                    return False
                stack.pop()

        return True if not stack else False

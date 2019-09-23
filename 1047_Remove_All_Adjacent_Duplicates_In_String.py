class Solution:
    def removeDuplicates(self, S: str) -> str:

        stack = []
        pointer = 0

        while pointer < len(S):

            letter = S[pointer]
            if not stack:
                stack.append(letter)
            else:
                if stack[-1] == letter:
                    stack.pop()
                else:
                    stack.append(letter)

            pointer += 1

        return "".join(stack)

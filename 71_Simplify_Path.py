class Solution:
    def simplifyPath(self, path: str) -> str:

        def get_substring(start):

            end = start + 1

            while end < len(path) and path[end] != "/":
                end += 1

            return path[start + 1:end], end

        stack = []
        current = 0

        while current < len(path):

            substring, current = get_substring(current)

            if substring == ".":
                continue

            elif substring == "..":
                if stack:
                    stack.pop()

            elif substring == "":
                continue

            else:
                stack.append(substring)

        ans = '/'.join(stack)
        ans = "/" + ans

        return ans

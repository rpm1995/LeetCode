class Solution:
    def checkRecord(self, s: str) -> bool:

        if len(s) == 1:
            return True

        if len(s) == 2:
            return False if s == "AA" else True

        if len(s) == 3:
            return False if "AA" in s or s == "LLL" else True

        a_count = 0

        for index in range(2):
            char = s[index]
            if char == "A":
                if a_count:
                    return False
                else:
                    a_count += 1

        for index in range(2, len(s)):
            char = s[index]

            if char == "A":
                if a_count:
                    return False
                else:
                    a_count += 1

            elif char == "L":
                if s[index - 2: index + 1] == "LLL":
                    return False

        return True

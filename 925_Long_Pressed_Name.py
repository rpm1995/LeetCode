class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        i = 0

        for j in range(len(typed)):

            if i < len(name) and name[i] == typed[j]:
                i += 1

            else:
                if j == 0 or typed[j] != typed[j - 1]:  # j=0 for specific test case
                    return False

        return i == len(name)

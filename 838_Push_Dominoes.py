class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        n = len(dominoes)
        forces = [0 for _ in range(n)]
        ans = ""

        force = 0

        for index, value in enumerate(dominoes):

            if value == "R":
                force = n
            elif value == "L":
                force = 0
            else:
                force = max(force - 1, 0)

            forces[index] = force

        force = 0

        for index in range(n - 1, -1, -1):
            value = dominoes[index]

            if value == "L":
                force = n
            elif value == "R":
                force = 0
            else:
                force = max(force - 1, 0)

            forces[index] -= force

        for index, value in enumerate(forces):

            if value == 0:
                ans += "."
            elif value < 0:
                ans += "L"
            else:
                ans += "R"

        return ans

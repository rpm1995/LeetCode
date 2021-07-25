class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = [[1]]

        for row in range(2, numRows + 1):
            res = [1 for _ in range(row)]

            for col in range(1, row - 1):
                res[col] = ans[-1][col - 1] + ans[-1][col]

            ans.append(res)

        return ans

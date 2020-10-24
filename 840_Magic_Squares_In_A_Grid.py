class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def all_vals_valid(row, col):

            numbers = set()

            for i in range(row, row + 3):
                for j in range(col, col + 3):

                    if 1 > grid[i][j] or grid[i][j] > 9 or grid[i][j] in numbers:
                        return False

                    numbers.add(grid[i][j])

            return True

        def rows_check(row, col):

            return sum(grid[row][col:col + 3]) == sum(grid[row + 1][col:col + 3]) == sum(grid[row + 2][col:col + 3])

        def cols_check(row, col):

            col1_sum = 0
            col2_sum = 0
            col3_sum = 0

            for i in range(row, row + 3):
                col1_sum += grid[i][col]

            for i in range(row, row + 3):
                col2_sum += grid[i][col + 1]

            for i in range(row, row + 3):
                col3_sum += grid[i][col + 2]

            return col1_sum == col2_sum == col3_sum

        def diags_check(row, col):

            diag_sum = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            antidiag_sum = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]

            return diag_sum == antidiag_sum

        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        if rows < 3 or cols < 3:
            return 0

        for i in range(rows - 2):
            for j in range(cols - 2):

                if all_vals_valid(i, j):

                    if rows_check(i, j) and cols_check(i, j) and diags_check(i, j):
                        ans += 1

        return ans

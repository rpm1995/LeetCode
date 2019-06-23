class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:

        rows = len(nums)
        cols = len(nums[0])

        if r * c > rows * cols:
            return nums

        values = []
        ans = [[0 for _ in range(c)] for _ in range(r)]
        index = 0

        for row in range(rows):
            for col in range(cols):
                values.append(nums[row][col])

        for row in range(r):
            for col in range(c):
                ans[row][col] = values[index]
                index += 1

        return ans

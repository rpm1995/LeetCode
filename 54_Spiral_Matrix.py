class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        ans = []

        left = 0
        right = cols - 1
        top = 0
        bottom = rows - 1

        while left < right and top < bottom:

            for i in range(left, right):
                ans.append(matrix[top][i])

            for i in range(top, bottom):
                ans.append(matrix[i][right])

            for i in range(right, left, -1):
                ans.append(matrix[bottom][i])

            for i in range(bottom, top, -1):
                ans.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if left == right and top == bottom:
            ans.append(matrix[left][top])

        elif top == bottom:
            ans.extend(matrix[top][left:right + 1])

        elif left == right:
            # ans.extend(matrix[top:bottom+1][left])
            for i in range(top, bottom + 1):
                ans.append(matrix[i][left])

        return ans

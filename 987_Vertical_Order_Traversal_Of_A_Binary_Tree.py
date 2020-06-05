# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        def dfs(node, row, col, ans):

            if node.left:
                dfs(node.left, row + 1, col - 1, ans)

            if node.right:
                dfs(node.right, row + 1, col + 1, ans)

            ans.append(list((col, row, node.val)))

            return

        def normalize(temp, ans):

            columns = {}
            minColumn = float('inf')
            maxColumn = -float('inf')

            for col, row, value in temp:

                if col not in columns:
                    columns[col] = []
                    minColumn = min(minColumn, col)
                    maxColumn = max(maxColumn, col)
                columns[col].append(value)

            for col in range(minColumn, maxColumn + 1):
                ans.append(columns[col])

            return

        row = 0
        col = 0
        temp = []
        ans = []

        dfs(root, row, col, temp)
        temp.sort(key=lambda x: (x[0], x[1], x[2]))
        normalize(temp, ans)

        return ans

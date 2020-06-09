# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:

        def helper(node, col, row, cols):

            if node.left:
                helper(node.left, col - 1, row + 1, cols)

            if node.right:
                helper(node.right, col + 1, row + 1, cols)

            if col not in cols:
                cols[col] = []
            cols[col].append([row, node.val])

            return

        if not root:
            return []

        mapping = {}
        helper(root, 0, 0, mapping)
        leftmost = min(mapping.keys())
        rightmost = max(mapping.keys())
        ans = []

        for col in range(leftmost, rightmost + 1):
            mapping[col].sort(key=lambda x: x[0])
            temp = []

            for row, val in mapping[col]:
                temp.append(val)
            ans.append(temp)

        return ans

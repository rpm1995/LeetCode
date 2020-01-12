# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.ans = 0

        def helper(node):
            if not node:
                return 0, 0

            L, L_count = helper(node.left)
            R, R_count = helper(node.right)

            numerator = node.val + L + R
            denominator = 1 + L_count + R_count

            average = numerator / denominator

            self.ans = max(self.ans, average)

            return numerator, denominator

        helper(root)
        return self.ans

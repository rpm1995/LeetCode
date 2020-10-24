# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def helper(node):

            if not node:
                return [float('inf'), -float('inf')]

            l_min, l_max = helper(node.left)
            r_min, r_max = helper(node.right)

            if l_min != float('inf'):
                self.ans = max(self.ans, abs(node.val - l_min))

            if r_min != float('inf'):
                self.ans = max(self.ans, abs(node.val - r_min))

            if l_max != -float('inf'):
                self.ans = max(self.ans, abs(node.val - l_max))

            if r_max != -float('inf'):
                self.ans = max(self.ans, abs(node.val - r_max))

            return [min(l_min, r_min, node.val), max(l_max, r_max, node.val)]

        self.ans = 0
        helper(root)

        return self.ans

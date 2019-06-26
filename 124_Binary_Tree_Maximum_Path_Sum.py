# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        if not root:
            return 0

        def helper(node):

            if not node:
                return 0

            L = helper(node.left)
            R = helper(node.right)

            self.max_ = max(self.max_, node.val + L + R, node.val, node.val + L, node.val + R)

            return max(node.val, node.val + L, node.val + R)

        self.max_ = -float('inf')
        helper(root)
        return self.max_

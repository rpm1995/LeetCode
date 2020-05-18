# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:

        def helper(node):

            if not node:
                return 0

            L = helper(node.left)
            R = helper(node.right)

            if node.left and node.left.val != node.val + 1:
                L = 0
            if node.right and node.right.val != node.val + 1:
                R = 0

            length = max(L, R) + 1
            self.ans = max(length, self.ans)
            return length

        self.ans = 0
        helper(root)
        return self.ans
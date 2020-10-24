# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0

            L = helper(node.left)
            R = helper(node.right)

            self.ans += abs(L) + abs(R)

            return node.val + L + R - 1

        self.ans = 0
        helper(root)

        return self.ans

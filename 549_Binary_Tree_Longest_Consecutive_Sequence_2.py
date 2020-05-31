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
                return [0, 0]

            inc = 1
            dcr = 1

            L = helper(node.left)
            R = helper(node.right)

            if node.left:
                if node.val == node.left.val + 1:
                    dcr = L[1] + 1
                elif node.val == node.left.val - 1:
                    inc = L[0] + 1

            if node.right:
                if node.val == node.right.val + 1:
                    dcr = max(dcr, 1 + R[1])
                elif node.val == node.right.val - 1:
                    inc = max(inc, 1 + R[0])

            self.ans = max(self.ans, inc + dcr - 1)
            return [inc, dcr]

        self.ans = 0
        helper(root)

        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def helper(self, node):

        if not node:
            return float('inf'), -float('inf'), 0, True

        L_min, L_max, L_size, L_isBST = self.helper(node.left)
        R_min, R_max, R_size, R_isBST = self.helper(node.right)

        if L_max < node.val < R_min:

            if L_isBST and R_isBST:
                self.ans = max(self.ans, L_size + R_size + 1)
                return min(L_min, R_min, node.val), max(L_max, R_max, node.val), L_size + R_size + 1, True

            elif L_isBST:
                self.ans = max(self.ans, L_size)
                return min(L_min, node.val), max(L_max, node.val), L_size + 1, False

            elif R_isBST:
                self.ans = max(self.ans, R_size)
                return min(R_min, node.val), max(R_max, node.val), R_size + 1, False

        return node.val, node.val, 0, False

    def largestBSTSubtree(self, root: TreeNode) -> int:

        self.ans = 0
        self.helper(root)

        return self.ans

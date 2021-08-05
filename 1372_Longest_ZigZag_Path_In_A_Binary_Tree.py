# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def traverse(self, node, direction, length):

        if not node:
            self.ans = max(self.ans, length - 1)
            return

        if direction == "R":
            self.traverse(node.left, "L", length + 1)
            self.traverse(node.right, "R", 1)

        else:
            self.traverse(node.right, "R", length + 1)
            self.traverse(node.left, "L", 1)

    def longestZigZag(self, root: TreeNode) -> int:

        self.ans = 0
        self.traverse(root.left, "L", 1)
        self.traverse(root.right, "R", 1)

        return self.ans

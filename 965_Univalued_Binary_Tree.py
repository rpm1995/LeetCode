# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        def helper(node, prev_value):

            if not node:
                return True

            if node.val != prev_value:
                return False

            L = helper(node.left, node.val)
            R = helper(node.right, node.val)

            return L and R

        return helper(root, root.val)

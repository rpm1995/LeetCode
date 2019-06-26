# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def helper(node):

            if not node:
                return False, None

            L, foundL = helper(node.left)
            R, foundR = helper(node.right)

            if L and R:
                return True, node

            if node != p and node != q:
                if L:
                    return True, foundL

                if R:
                    return True, foundR

            if node == p or node == q:
                return True, node

            return False, None

        return helper(root)[1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, mini, maxi):

            if not node:
                return True

            if node.val <= mini or node.val >= maxi:
                return False

            L = helper(node.left, mini, node.val)
            R = helper(node.right, node.val, maxi)

            return L and R

        return helper(root, -float('inf'), float('inf'))

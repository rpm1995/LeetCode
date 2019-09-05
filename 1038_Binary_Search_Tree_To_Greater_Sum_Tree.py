# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        self.total = 0

        def helper(node):

            if node.right:
                helper(node.right)

            node.val += self.total
            self.total = node.val

            if node.left:
                helper(node.left)

        helper(root)
        return root

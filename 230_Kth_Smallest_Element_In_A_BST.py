# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Think Inorder Traversal

        def helper(node):

            if not node:
                return

            helper(node.left)
            self.k -= 1

            if self.k == 0:
                self.ans = node.val
                return

            helper(node.right)

        self.k = k
        self.ans = 0
        helper(root)
        return self.ans

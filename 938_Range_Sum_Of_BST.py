# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        #         self.ans = 0

        #         def helper(node):

        #             if not node:
        #                 return

        #             if L <= node.val <= R:
        #                 self.ans += node.val
        #             helper(node.left)
        #             helper(node.right)

        #         helper(root)

        #         return self.ans

        def helper(node):

            if not node:
                return 0

            if node.val < L:
                return helper(node.right)
            elif node.val > R:
                return helper(node.left)
            else:
                return helper(node.left) + node.val + helper(node.right)

        return helper(root)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        self.difference = float('inf')
        self.ans = 0

        def helper(node):

            if not node:
                return

            difference = abs(target - node.val)

            if difference < self.difference:
                self.ans = node.val
                self.difference = difference

            if target < node.val:
                helper(node.left)
            else:
                helper(node.right)

        if not root:
            return 0

        helper(root)
        return self.ans

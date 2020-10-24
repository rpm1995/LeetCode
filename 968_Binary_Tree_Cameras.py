# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        # 0 : monitored, no cam
        # 1 : monitored, cam here
        # 2 : unmonitored

        def helper(node):

            if not node:
                return 0

            L = helper(node.left)
            R = helper(node.right)

            if L == 2 or R == 2:
                node.val = 1
                self.ans += 1

            elif L == 1 or R == 1:
                node.val = 0

            else:
                node.val = 2

            return node.val

        self.ans = 0
        if helper(root) == 2:
            self.ans += 1

        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def helper(node1, node2):

            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            path_one = helper(node1.left, node2.right)
            path_two = helper(node1.right, node2.left)

            return path_one and path_two

        if not root:
            return True

        return helper(root.left, root.right)

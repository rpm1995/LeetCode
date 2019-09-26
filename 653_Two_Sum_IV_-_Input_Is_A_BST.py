# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        node_values = set()

        def helper(node):

            if not node:
                return False

            difference = k - node.val

            if difference in node_values:
                return True

            node_values.add(node.val)

            L = helper(node.left)
            R = helper(node.right)

            return L or R

        return helper(root)

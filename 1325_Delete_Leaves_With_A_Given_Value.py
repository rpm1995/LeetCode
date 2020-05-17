# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        def helper(node):

            if not node:
                return None

            node.left = helper(node.left)
            node.right = helper(node.right)

            if not node.left and not node.right:
                if node.val == target:
                    node = None
                    return node

            return node

        retme = helper(root)
        return retme

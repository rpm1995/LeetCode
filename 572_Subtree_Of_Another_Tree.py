# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def compare(node1, node2):

            if not node1 and not node2:
                return True

            if not node1 and node2:
                return False

            if node1 and not node2:
                return False

            if node1.val != node2.val:
                return False

            L = compare(node1.left, node2.left)
            R = compare(node1.right, node2.right)

            return L and R

        def traverse(s):

            if not s:
                return False

            if s.val == t.val:
                if compare(s, t):
                    return True

            L = traverse(s.left)
            R = traverse(s.right)

            return L or R

        return traverse(s)

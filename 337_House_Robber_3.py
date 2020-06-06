# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # def helper(node):
        #     if not node:
        #         return 0
        #
        #     L = helper(node.left)
        #     R = helper(node.right)
        #     Lgl = helper(node.left.left) if node.left else 0
        #     Lgr = helper(node.left.right) if node.left else 0
        #     Rgl = helper(node.right.left) if node.right else 0
        #     Rgr = helper(node.right.right) if node.right else 0
        #
        #     return max(node.val + Lgl + Lgr + Rgl + Rgr, L + R)
        #
        # ans = helper(root)
        # return ans

        from collections import deque

        # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
        class Solution:
            def rob(self, root: TreeNode) -> int:

                def helper(node, cache):

                    if not node:
                        return 0

                    if node in cache:
                        return cache[node]

                    L = helper(node.left, cache)
                    R = helper(node.right, cache)
                    Lgl = helper(node.left.left, cache) if node.left else 0
                    Lgr = helper(node.left.right, cache) if node.left else 0
                    Rgl = helper(node.right.left, cache) if node.right else 0
                    Rgr = helper(node.right.right, cache) if node.right else 0

                    cache[node] = max(node.val + Lgl + Lgr + Rgl + Rgr, L + R)
                    return cache[node]

                cache = {}
                ans = helper(root, cache)
                return ans

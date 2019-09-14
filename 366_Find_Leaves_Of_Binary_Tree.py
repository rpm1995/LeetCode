# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:

        res_dict = {}
        res = []

        def helper(node):

            if not node:
                return 0

            L = helper(node.left)
            R = helper(node.right)

            current_level = max(L, R) + 1

            if current_level not in res_dict:
                res_dict[current_level] = []
            res_dict[current_level].append(node.val)

            return current_level

        helper(root)

        for level in range(1, len(res_dict) + 1):
            res.append(res_dict[level])

        return res

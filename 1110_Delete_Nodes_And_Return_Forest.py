# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        def helper(node, parent_exists):

            if not node:
                return None

            if node.val in to_delete:
                node.left = helper(node.left, False)
                node.right = helper(node.right, False)

                return None

            else:
                if not parent_exists:
                    ans.append(node)
                node.left = helper(node.left, True)
                node.right = helper(node.right, True)

                return node

        ans = []
        to_delete = set(to_delete)
        helper(root, False)

        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def build(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        inorder_index = inorder.index(root.val)

        left_inorder_subtree = inorder[: inorder_index]
        right_inorder_subtree = inorder[inorder_index + 1:]
        left_postorder_subtree = postorder[: inorder_index]
        right_postorder_subtree = postorder[inorder_index: -1]

        root.left = self.build(left_inorder_subtree, left_postorder_subtree)
        root.right = self.build(right_inorder_subtree, right_postorder_subtree)

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(inorder, postorder)

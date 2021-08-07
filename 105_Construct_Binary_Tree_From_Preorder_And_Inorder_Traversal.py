# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def build(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        node = TreeNode(preorder[0])
        inorder_index = inorder.index(node.val)

        left_subtree_inorder = inorder[: inorder_index]
        right_subtree_inorder = inorder[inorder_index + 1:]
        left_subtree_preorder = preorder[1: inorder_index + 1]
        right_subtree_preorder = preorder[inorder_index + 1:]

        node.left = self.build(left_subtree_preorder, left_subtree_inorder)
        node.right = self.build(right_subtree_preorder, right_subtree_inorder)

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, inorder)

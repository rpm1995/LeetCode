# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:

        def helper(node):

            if not node:
                return -float('inf'), True

            L, left_tree_true = helper(node.left)
            R, right_tree_true = helper(node.right)
            current_subtree_true = False

            if L == -float('inf') and R == -float('inf'):
                self.ans += 1
                current_subtree_true = True

            elif (L == -float('inf') and R == node.val and right_tree_true is True) or (
                    L == node.val and R == -float('inf') and left_tree_true is True):
                self.ans += 1
                current_subtree_true = True

            elif L == node.val and R == node.val and left_tree_true and right_tree_true:
                self.ans += 1
                current_subtree_true = True

            return node.val, current_subtree_true

        self.ans = 0
        helper(root)

        return self.ans


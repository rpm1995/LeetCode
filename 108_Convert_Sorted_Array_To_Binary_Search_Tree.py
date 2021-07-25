# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, arr):
        if not arr:
            return None

        mid = len(arr) // 2

        root = TreeNode(arr[mid])
        root.left = self.helper(arr[: mid])
        root.right = self.helper(arr[mid + 1:])

        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums)

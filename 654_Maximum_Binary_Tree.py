# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def helper(arr):
            if not arr:
                return None

            max_element = max(arr)
            max_element_index = arr.index(max(arr))
            left_arr = arr[: max_element_index]
            right_arr = arr[max_element_index + 1:]
            new_node = TreeNode(max_element)

            new_node.left = helper(left_arr)
            new_node.right = helper(right_arr)

            return new_node

        return helper(nums)

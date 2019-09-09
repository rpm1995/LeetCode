from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        queue = deque([])
        queue.append((1, root))
        max_sum = -float('inf')
        max_level = 1

        while queue:

            number_of_children = len(queue)
            level_sum = 0
            level = 1

            while number_of_children:

                level, node = queue.popleft()
                level_sum += node.val
                number_of_children -= 1

                if node.left:
                    queue.append((level + 1, node.left))
                if node.right:
                    queue.append((level + 1, node.right))

            if level_sum > max_sum:
                max_sum = max(max_sum, level_sum)
                max_level = level

        return max_level

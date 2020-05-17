from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:

        def containsNode(nodes):

            for node in nodes:
                if node is not None:
                    return True

            return False

        queue = deque([])
        queue.append(root)

        while queue:

            node = queue.popleft()

            if not node:
                if containsNode(queue) is True:
                    return False

            else:
                queue.append(node.left)
                queue.append(node.right)

        return True

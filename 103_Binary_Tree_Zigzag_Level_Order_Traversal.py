from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        queue = deque([])
        queue.append(root)
        ans = []
        left_to_right = True

        while queue:

            children_number = len(queue)
            children = []

            while children_number:
                child = queue.popleft()

                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)

                children.append(child.val)
                children_number -= 1

            if left_to_right is False:
                children.reverse()

            ans.append(children)
            left_to_right = not left_to_right

        return ans

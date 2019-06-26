from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        queue = deque([])
        queue.append(root)
        ans = []

        while queue:

            children_number = len(queue)
            children = []

            while children_number > 0:
                child = queue.popleft()
                children.append(child.val)

                if child.left:
                    queue.append(child.left)

                if child.right:
                    queue.append(child.right)

                children_number -= 1

            ans.append(children)

        return ans

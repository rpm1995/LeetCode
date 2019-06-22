from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        queue = deque([])
        queue.append(root)
        ans = []

        while queue:

            num_children = len(queue)
            children = []

            while num_children:
                children.append(queue.popleft())
                num_children -= 1

            placeholder = float('inf')

            for child in children:
                if child.left:
                    queue.append(child.left)

                if child.right:
                    queue.append(child.right)

                placeholder = child.val

            ans.append(placeholder)

        return ans


from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        def dfs(node, parent):

            if not node:
                return

            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        parents = {}
        dfs(root, None)

        queue = deque([(target, 0)])
        # seen = set(target)
        seen = {target}
        ans = []

        while queue:

            node, distance = queue.popleft()

            if distance == K:

                ans.append(node.val)

                for neighbour, dist in queue:
                    ans.append(neighbour.val)

                return ans

            if node.left and node.left not in seen:
                seen.add(node.left)
                queue.append((node.left, distance + 1))

            if node.right and node.right not in seen:
                seen.add(node.right)
                queue.append((node.right, distance + 1))

            parent = parents[node]
            if parent and parent not in seen:
                seen.add(parent)
                queue.append((parent, distance + 1))

        return []

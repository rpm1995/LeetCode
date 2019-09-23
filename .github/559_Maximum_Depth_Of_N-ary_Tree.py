"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        self.ans = 0

        def helper(node, length):

            length += 1
            self.ans = max(self.ans, length)

            for child in node.children:
                helper(child, length)

            return

        if not root:
            return 0

        helper(root, 0)

        return self.ans

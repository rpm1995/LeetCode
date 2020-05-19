"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def helper(node):

            if not node:
                return

            head = node

            while head:
                if head.left:
                    head.left.next = head.right
                    head.right.next = head.next.left if head.next else None
                head = head.next

            helper(node.left)

        helper(root)
        return root

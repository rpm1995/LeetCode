"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        old_new = {None: None}
        old_node = head

        while old_node:

            new_node = Node(old_node.val)
            old_new[old_node] = new_node
            old_node = old_node.next

        old_node = head

        while old_node:

            old_new[old_node].next = old_new[old_node.next]
            old_new[old_node].random = old_new[old_node.random]
            old_node = old_node.next

        return old_new[head]

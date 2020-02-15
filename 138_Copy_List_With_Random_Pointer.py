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
        old_head = head

        while old_head:
            new_node = Node(old_head.val, None, None)
            old_new[old_head] = new_node
            old_head = old_head.next

        retme = Node(-1)
        new_head = retme
        old_head = head

        while old_head:
            new_head.next = old_new[old_head]
            new_head = new_head.next
            new_head.random = old_new[old_head.random]
            old_head = old_head.next

        return retme.next

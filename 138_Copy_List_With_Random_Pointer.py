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

        old_new = {None: None}
        ptr = head

        while ptr:
            new_node = Node(ptr.val)
            old_new[ptr] = new_node
            ptr = ptr.next

        dummy = Node(-1)
        new_ptr = dummy
        ptr = head

        while ptr:

            new_ptr.next = old_new[ptr]
            new_ptr = new_ptr.next
            new_ptr.random = old_new[ptr.random]
            ptr = ptr.next

        return dummy.next

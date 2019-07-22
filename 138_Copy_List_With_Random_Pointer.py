"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        dicti = {None: None}
        ptr = head

        while ptr:
            new_node = Node(ptr.val, None, None)
            dicti[ptr] = new_node
            ptr = ptr.next

        ptr = head
        dummy = Node(0, None, None)
        ans_ptr = dummy

        while ptr:
            ans_ptr.next = dicti[ptr]
            ans_ptr = ans_ptr.next
            ans_ptr.next = dicti[ptr.next]
            ans_ptr.random = dicti[ptr.random]
            ptr = ptr.next

        return dummy.next

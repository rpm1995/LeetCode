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

        node = head

        while node:
            dicti[node] = Node(node.val, None, None)
            node = node.next

        node = head
        ptr = Node(0, None, None)
        retme = ptr

        while node:
            ptr.next = dicti[node]
            ptr = ptr.next
            ptr.random = dicti[node.random]
            node = node.next

        return retme.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def swap_two(self, node):

        if not node:
            return None

        if not node.next:
            return node

        temp = node.next.next
        node.next.next = node
        retme = node.next
        node.next = self.swap_two(temp)

        return retme

    def swapPairs(self, head: ListNode) -> ListNode:

        return self.swap_two(head)

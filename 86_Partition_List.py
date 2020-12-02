# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        lower = ListNode(0)
        lower_head = lower
        higher = ListNode(0)
        higher_head = higher
        ptr = head

        while ptr:

            value = ptr.val

            if value < x:
                lower.next = ptr
                lower = lower.next

            else:
                higher.next = ptr
                higher = higher.next

            ptr = ptr.next

        lower.next = higher_head.next
        higher.next = None

        return lower_head.next

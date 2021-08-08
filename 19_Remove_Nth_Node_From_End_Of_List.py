# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = None
        cur = head
        end = head

        while n:
            end = end.next
            n -= 1

        while end:
            prev = cur
            cur = cur.next
            end = end.next

        if not prev:
            return head.next

        prev.next = cur.next

        return head

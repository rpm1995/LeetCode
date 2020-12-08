# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        tortoise = head
        hare = head
        cycle_exists = False

        if not hare or not hare.next:
            return None

        while hare.next and hare.next.next:

            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                cycle_exists = True
                break

        if not cycle_exists:
            return None

        tortoise = head

        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next

        return tortoise

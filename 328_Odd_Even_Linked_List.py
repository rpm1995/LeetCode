# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head:
            return None

        odd_head = head
        even_head = head.next
        odd_head_copy = odd_head
        even_head_copy = even_head

        while odd_head.next and odd_head.next.next:
            odd_head.next = odd_head.next.next
            odd_head = odd_head.next
            even_head.next = even_head.next.next
            even_head = even_head.next

        odd_head.next = even_head_copy
        return odd_head_copy

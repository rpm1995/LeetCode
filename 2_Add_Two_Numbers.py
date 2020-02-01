# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(-1)
        retme = head
        carry = 0

        while l1 or l2:

            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val

            sum_ = val1 + val2 + carry
            carry = sum_ // 10
            sum_ %= 10

            head.next = ListNode(sum_)
            head = head.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            head.next = ListNode(1)

        return retme.next

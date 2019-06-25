# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2

        if not l2:
            return l1

        carry = 0
        retme = ListNode(None)
        node = retme

        while l1 or l2 or carry:
            sum_ = 0

            if l1:
                sum_ += l1.val
                l1 = l1.next

            if l2:
                sum_ += l2.val
                l2 = l2.next

            sum_ += carry

            if sum_ >= 10:
                carry = 1
                sum_ %= 10

            else:
                carry = 0

            node.next = ListNode(sum_)
            node = node.next

        return retme.next

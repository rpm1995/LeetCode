# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def get_number(head):

            number = 0

            while head:
                number = number * 10 + head.val
                head = head.next

            return number

        def reverse_list(node):

            prev = None
            cur = node
            next_ = node.next

            while cur:
                cur.next = prev
                prev = cur
                cur = next_

                if next_:
                    next_ = next_.next

            return prev

        first_number = get_number(l1)
        second_number = get_number(l2)
        sum_ = first_number + second_number
        dummy = head = ListNode(0)

        if sum_ == 0:
            return dummy

        while sum_:
            digit = sum_ % 10
            sum_ = sum_ // 10
            head.next = ListNode(digit)
            head = head.next

        return reverse_list(dummy.next)

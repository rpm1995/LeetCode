# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        len1 = 0
        len2 = 0
        head1 = headA
        head2 = headB

        while head1:
            len1 += 1
            head1 = head1.next

        while head2:
            len2 += 1
            head2 = head2.next

        difference = abs(len1 - len2)

        if len1 < len2:
            headA, headB = headB, headA

        while difference:
            headA = headA.next
            difference -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

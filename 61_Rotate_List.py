# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        def getLen(ptr):

            length = 0

            while ptr:
                length += 1
                ptr = ptr.next

            return length

        length = getLen(head)

        if length == 0:
            return None

        if k >= length:
            k %= length

        if k == 0:
            return head

        ptr = head
        end = head
        count = 0

        while count < k:
            ptr = ptr.next
            count += 1

        while ptr.next is not None:
            end = end.next
            ptr = ptr.next

        after_end = end.next
        ptr.next = head
        end.next = None

        return after_end

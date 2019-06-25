# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        retme = ListNode(None)
        new_list = retme

        while l1 or l2:

            if l1 and l2:
                if l1.val <= l2.val:
                    new_list.next = l1
                    new_list = new_list.next
                    l1 = l1.next

                else:
                    new_list.next = l2
                    new_list = new_list.next
                    l2 = l2.next

            elif l1:
                new_list.next = l1
                break

            elif l2:
                new_list.next = l2
                break

        return retme.next

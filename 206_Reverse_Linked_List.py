# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return None

        prev = None
        cur = head
        nex = head.next

        while cur:

            cur.next = prev
            prev = cur
            cur = nex

            if nex:
                nex = nex.next

        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node):
            if not node or not node.next:
                self.head = node
                return node

            reverse(node.next)
            node.next.next = node
            node.next = None

            return node

        self.head = ListNode(-1)
        reverse(head)
        return self.head


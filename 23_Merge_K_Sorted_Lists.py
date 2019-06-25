import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        heap = []
        heapq.heapify(heap)
        ans = retme = ListNode(None)

        for index, linked_list in enumerate(lists):

            if linked_list:
                heapq.heappush(heap, (linked_list.val, index, linked_list))

        while heap:

            _, index, node = heapq.heappop(heap)

            ans.next = node
            node = node.next
            ans = ans.next

            if node:
                heapq.heappush(heap, (node.val, index, node))

        return retme.next

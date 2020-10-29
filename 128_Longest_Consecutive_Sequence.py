# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         nums_set = set(nums)
#         ans = 0
#
#         for num in nums:
#
#             if num - 1 not in nums_set:  # This one single line guarantees linear time
#                 temp_ans = 1
#
#                 while num + 1 in nums_set:
#                     temp_ans += 1
#                     num += 1
#
#                 ans = max(ans, temp_ans)
#
#         return ans

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        parents = {}
        size = {}

        if not nums:
            return 0

        def find(node):

            if parents[node] != node:
                parents[node] = find(parents[node])

            return parents[node]

        def union(node1, node2):

            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                parents[root1] = root2
                size[root2] += size[root1]

        for num in nums:
            parents[num] = num
            size[num] = 1

        for num in nums:

            if num - 1 in nums:
                union(num, num - 1)

            if num + 1 in nums:
                union(num, num + 1)

        return max(size.values())

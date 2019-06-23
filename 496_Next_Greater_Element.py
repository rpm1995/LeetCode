class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1:
            return []

        if not nums2:
            return [-1 for _ in range(len(nums1))]

        stack = []
        next_greater = {}
        ans = []

        for index, num in enumerate(nums2):

            if not stack or num < stack[-1]:
                stack.append(num)

            else:

                while stack and stack[-1] < num:
                    next_greater[stack.pop()] = num

                stack.append(num)

        for num in stack:
            next_greater[num] = -1

        for num in nums1:
            ans.append(next_greater[num])

        return ans

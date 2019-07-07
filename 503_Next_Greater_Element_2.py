class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        #         n = len(nums)
        #         ans = [-1 for _ in range(n)]

        #         for i in range(len(nums)):
        #             current_num = nums[i]

        #             for j in range(len(nums)):
        #                 next_num = nums[(i+j)%n]

        #                 if next_num > current_num:
        #                     ans[i] = next_num
        #                     break

        #         return ans

        n = len(nums)
        res = [-1 for _ in range(n)]
        stack = []

        for i in range(2 * n):

            current_index = i % n
            current_element = nums[current_index]

            if not stack or current_element < nums[stack[-1]]:
                stack.append(current_index)

            else:
                while stack and current_element > nums[stack[-1]]:
                    top = stack.pop()

                    if res[top] == -1:
                        res[top] = current_element

                stack.append(current_index)

        return res

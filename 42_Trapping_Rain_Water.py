class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        index = 0
        area = 0

        while index < len(height):

            if not stack or height[index] <= height[stack[-1]]:
                stack.append(index)
                index += 1

            else:
                top = stack.pop()
                if stack:
                    width = index - stack[-1] - 1
                    hight = min(height[stack[-1]], height[index]) - height[top]
                    area += width * hight

        return area

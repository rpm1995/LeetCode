class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        horizontalCuts.sort()
        verticalCuts.sort()

        max_height = horizontalCuts[0]
        max_width = verticalCuts[0]

        index = 1

        while index < len(verticalCuts):
            max_width = max(max_width, verticalCuts[index] - verticalCuts[index - 1])
            index += 1

        index = 1

        while index < len(horizontalCuts):
            max_height = max(max_height, horizontalCuts[index] - horizontalCuts[index - 1])
            index += 1

        max_height = max(max_height, h - horizontalCuts[-1])
        max_width = max(max_width, w - verticalCuts[-1])

        return max_width * max_height % ((10 ** 9) + 7)

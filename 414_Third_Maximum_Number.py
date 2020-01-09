class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        first = -float('inf')
        second = -float('inf')
        third = -float('inf')

        for num in nums:

            if num != first and num != second and num != third:

                if num > first:
                    third = second
                    second = first
                    first = num

                elif num > second:
                    third = second
                    second = num

                elif num > third:
                    third = num

        return third if third != -float('inf') else first

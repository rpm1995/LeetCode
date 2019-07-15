class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        small = float('inf')
        big = float('inf')

        for num in nums:

            if num <= small:
                small = num

            elif num <= big:
                big = num

            else:  # The = sign in previous comparisons ensure that this is true iff num is bigger than small and big
                return True

        return False

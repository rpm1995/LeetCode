class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        n = len(arr)
        cumsum = {0: -1}  # sum: index
        found_left = False
        ans = float('inf')
        left_size = float('inf')
        right_size = float('inf')

        running_sum = 0

        for index, value in enumerate(arr):
            running_sum += value
            cumsum[running_sum] = index

        running_sum = 0

        for index, value in enumerate(arr):

            running_sum += value
            to_find_left = running_sum - target

            if to_find_left in cumsum:
                left_size = min(left_size, index - cumsum[to_find_left])
                found_left = True

            to_find_right = running_sum + target
            if found_left and to_find_right in cumsum:
                # right_size = min(right_size, cumsum[to_find_right] - index)

                ans = min(ans, left_size + cumsum[to_find_right] - index)  # Can't do left_size+right_size!

        return -1 if ans == float('inf') else ans

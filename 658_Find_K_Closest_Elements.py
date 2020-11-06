# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         # O(n) Solution
#         left = 0
#         right = len(arr) - 1
#
#         while right - left + 1 > k:
#
#             if abs(arr[left] - x) > abs(arr[right] - x):
#                 left += 1
#
#             else:
#                 right -= 1
#
#         return arr[left: right + 1]


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # approach: use binary search to find the start which is closest to x

        left = 0
        right = len(arr) - k

        while left < right:
            mid = left + (right - left) // 2

            # mid + k is closer to x, discard mid by assigning left = mid + 1
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1

            # mid is equal or closer to x than mid + k, remains mid as candidate
            else:
                right = mid

        # left == right, which makes both left and left + k have same diff with x
        return arr[left: left + k]

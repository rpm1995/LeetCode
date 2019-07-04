class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def binary_search(array, target):

            left = 0
            right = len(array) - 1

            while left <= right:

                mid = (left + right) // 2

                if array[mid] == target:
                    return True
                elif array[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False


        nums2.sort()
        ans = set()

        for num in nums1:
            if binary_search(nums2, num) is True:
                ans.add(num)

        ans = list(ans)
        return ans

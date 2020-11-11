class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        def mergeAndCount(arr, start, end, result):

            if start >= end:
                return

            mid = (start + end) // 2
            mergeAndCount(arr, start, mid, result)
            mergeAndCount(arr, mid + 1, end, result)

            left = start
            right = mid + 1
            numElements = 0
            merged = []

            while left < mid + 1 and right <= end:

                if arr[left][0] > arr[right][0]:

                    numElements += 1
                    merged.append(arr[right])
                    right += 1

                else:

                    result[arr[left][1]] += numElements
                    merged.append(arr[left])
                    left += 1

            while left < mid + 1:
                result[arr[left][1]] += numElements
                merged.append(arr[left])
                left += 1

            while right <= end:
                merged.append(arr[right])
                right += 1

            position = start

            for value in merged:
                arr[position] = value
                position += 1

        for index, value in enumerate(nums):
            nums[index] = (value, index)

        result = [0 for _ in range(len(nums))]
        mergeAndCount(nums, 0, len(nums) - 1, result)

        return result

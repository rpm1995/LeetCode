import heapq


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #
        #         heap = []
        #         heapq.heapify(heap)

        #         for num in nums:

        #             if len(heap) >= k:
        #                 heapq.heappushpop(heap, num)
        #             else:
        #                 heapq.heappush(heap, num)

        #         return heapq.heappop(heap)

    def partition(self, nums, left, right):

        pivot = nums[right]
        index = left

        for j in range(left, right):

            if nums[j] < pivot:
                nums[j], nums[index] = nums[index], nums[j]
                index += 1

        nums[index], nums[right] = nums[right], nums[index]

        return index

    def quick_sort(self, nums, start, end):

        if start > end:
            return num

        pivot_index = self.partition(nums, start, end)

        if pivot_index == self.k:
            return nums[pivot_index]

        if pivot_index < self.k:
            return self.quick_sort(nums, pivot_index + 1, end)

        elif pivot_index > self.k:
            return self.quick_sort(nums, start, pivot_index - 1)

    def findKthLargest(self, nums: List[int], k: int) -> int:

        self.k = len(nums) - k
        return self.quick_sort(nums, 0, len(nums) - 1)

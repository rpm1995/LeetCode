import ddddddddddddddheapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        #         heap = []
        #         heapq.heapify(heap)

        #         for num in nums:

        #             if len(heap) >= k:
        #                 heapq.heappushpop(heap, num)
        #             else:
        #                 heapq.heappush(heap, num)

        #         return heapq.heappop(heap)

        def partition(left, right, pivot_index):

            pivot = nums[pivot_index]

            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]

            store = left

            for i in range(left, right):

                if nums[i] < pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1

            nums[right], nums[store] = nums[store], nums[right]

            return store

        def select(left, right, kth_smallest):

            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)

            pivot_index = partition(left, right, pivot_index)

            if kth_smallest == pivot_index:
                return nums[kth_smallest]
            elif kth_smallest > pivot_index:
                return select(pivot_index + 1, right, kth_smallest)
            else:
                return select(left, pivot_index - 1, kth_smallest)

        return select(0, len(nums) - 1, len(nums) - k)

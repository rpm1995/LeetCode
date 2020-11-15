class SparseVector:
    def __init__(self, nums: List[int]):

        self.hash = {}

        for index, value in enumerate(nums):

            if value != 0:
                self.hash[index] = value

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        ans = 0

        for key, val in vec.hash.items():

            if val != 0 and key in self.hash:
                ans += self.hash[key] * val

        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if letters[-1] <= target:
            return letters[0]

        left = 0
        right = len(letters) - 1

        while left < right:

            mid = (left + right) // 2

            if letters[mid] == target:
                # if mid < len(letters) - 1:
                #     return letters[mid+1]
                # else:
                #     return letters[0]
                left = mid + 1

            elif letters[mid] < target:
                left = mid + 1

            elif letters[mid] > target:
                right = mid

        return letters[left]

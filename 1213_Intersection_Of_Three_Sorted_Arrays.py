class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        first = 0
        second = 0
        third = 0
        ans = []
        first_len = len(arr1)
        second_len = len(arr2)
        third_len = len(arr3)

        while first < first_len and second < second_len and third < third_len:

            if arr1[first] == arr2[second] == arr3[third]:
                ans.append(arr1[first])
                first += 1
                second += 1
                third += 1

            elif arr1[first] < arr2[second]:
                first += 1

            elif arr2[second] < arr3[third]:
                second += 1

            else:
                third += 1

        return ans

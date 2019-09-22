class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        elements = {}
        ans = []

        for element in arr1:
            if element not in elements:
                elements[element] = 0
            elements[element] += 1

        pointer2 = 0

        while pointer2 < len(arr2):

            element = arr2[pointer2]

            while elements[element] > 0:
                ans.append(element)
                elements[element] -= 1

            del elements[element]
            pointer2 += 1

        while elements:

            for element in range(0, 1001):

                if element in elements:
                    while elements[element] > 0:
                        ans.append(element)
                        elements[element] -= 1

                    del elements[element]

        return ans

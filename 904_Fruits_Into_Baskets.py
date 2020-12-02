class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        fruits = {}
        left = 0
        ans = 0

        for right, fruit in enumerate(tree):

            if fruit not in fruits:
                fruits[fruit] = 0
            fruits[fruit] += 1

            while left < right and len(fruits) > 2:

                left_fruit = tree[left]

                if fruits[left_fruit] == 1:
                    del fruits[left_fruit]
                else:
                    fruits[left_fruit] -= 1

                left += 1

            ans = max(ans, right - left + 1)

        return ans

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def helper(current, depth):

            res = 0

            for item in current:
                if item.isInteger():
                    res += item.getInteger() * depth
                else:
                    res += helper(item.getList(), depth + 1)

            return res

        return helper(nestedList, 1)
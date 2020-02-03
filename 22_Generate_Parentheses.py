class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 1:
            return ["()"]

        if n == 0:
            return []

        left = 0
        right = 0

        def helper(res, ans, left, right):

            if left == n and right == n:
                ans.append(res)

            else:

                if right <= left:
                    if left < n:
                        helper(res + "(", ans, left + 1, right)

                    if right < n and right < left:
                        helper(res + ")", ans, left, right + 1)

            return ans

        return helper("", [], left, right)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def helper(left, right, res, ans):

            if left == right and left == n:
                ans.append(res)
                return

            if left > n or right > left:
                return

            helper(left + 1, right, res + "(", ans)
            helper(left, right + 1, res + ")", ans)

        helper(0, 0, "", ans)
        return ans

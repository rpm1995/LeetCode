class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapping = {"2": "abc",
                   "3": "def",
                   "4": "ghi",
                   "5": "jkl",
                   "6": "mno",
                   "7": "pqrs",
                   "8": "tuv",
                   "9": "wxyz"}
        ans = []

        if not digits:
            return ans

        def helper(digits, index, res, ans):

            if index == len(digits):
                ans.append(res)
                return

            current_digit = digits[index]

            for current_char in mapping[current_digit]:
                helper(digits, index + 1, res + current_char, ans)

            return

        helper(digits, 0, "", ans)
        return ans

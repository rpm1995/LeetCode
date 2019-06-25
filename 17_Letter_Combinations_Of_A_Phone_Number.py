class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapping = {2: ["a", "b", "c"],
                   3: ["d", "e", "f"],
                   4: ["g", "h", "i"],
                   5: ["j", "k", "l"],
                   6: ["m", "n", "o"],
                   7: ["p", "q", "r", "s"],
                   8: ["t", "u", "v"],
                   9: ["w", "x", "y", "z"]}

        if not digits:
            return []

        def helper(remaining, ans, res):

            if not remaining:
                ans.append(res)

            else:
                current = int(remaining[0])
                remaining = remaining[1:]

                for alphabets in mapping[current]:
                    res += alphabets
                    helper(remaining, ans, res)
                    res = res[:-1]

            return ans

        return helper(digits, [], "")

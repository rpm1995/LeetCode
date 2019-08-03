class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def ispalin(string):
            return string[::] == string[::-1]

        def helper(res, cur_index):

            if cur_index == len(s):
                ans.append(res[:])

            else:

                for next_index in range(cur_index + 1, len(s) + 1):
                    if ispalin(s[cur_index: next_index]) is True:
                        res.append(s[cur_index: next_index])
                        helper(res, next_index)
                        res.pop()

        ans = []
        helper([], 0)

        return ans

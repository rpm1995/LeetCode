class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        romans = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        ans = 0

        for i in range(len(s) - 1):
            if romans[s[i]] < romans[s[i + 1]]:
                ans -= romans[s[i]]
            else:
                ans += romans[s[i]]

        ans += romans[s[-1]]
        return ans

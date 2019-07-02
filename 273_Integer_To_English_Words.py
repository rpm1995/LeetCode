class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        def helper(num):

            if num == 0:
                return ""

            if num < 20:
                return less_than_twenty[num] + " "

            elif num < 100:
                return tens[num / 10] + " " + helper(num % 10)

            else:
                return less_than_twenty[num / 100] + " Hundred " + helper(num % 100)

        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        less_than_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                            "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        thousands = ["", "Thousand", "Million", "Billion"]

        ans = ""
        i = 0

        if num == 0:
            return "Zero"

        while num > 0:

            if num % 1000 != 0:
                ans = helper(num % 1000) + thousands[i] + " " + ans

            num /= 1000
            i += 1

        return ans.strip()

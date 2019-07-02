class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False

        if x < 0:
            negative = True

        # x = str(abs(x))
        # y = ""

        #         for i in range(len(x) - 1, -1 ,-1):
        #             y += x[i]

        #         if negative is True:
        #             y = "-" + y
        #         y.strip()

        #         if int(y) < -2**31 or int(y) > (2**31) -1:
        #             return 0
        #         return int(y)

        x = abs(x)
        y = 0

        while x:
            y = (y * 10) + (x % 10)
            x = x // 10

        if negative:
            y *= -1

        return y if -2 ** 31 < y < 2 ** 31 else 0

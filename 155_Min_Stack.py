class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # self.thehelp = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # self.stack.append(x)
        # if not self.thehelp or self.thehelp[-1] > x:
        #     self.thehelp.append(x)
        # else:
        #     self.thehelp.append(self.thehelp[-1])

        value = x
        min_ = float('inf')

        if not self.stack or self.stack[-1][1] > value:
            min_ = value
        else:
            min_ = self.stack[-1][1]

        self.stack.append((value, min_))

    def pop(self):
        """
        :rtype: void
        """
        value, min_ = self.stack.pop()
        # self.thehelp.pop()
        return value

    def top(self):
        """
        :rtype: int
        """
        value, min_ = self.stack[-1]
        return value
        # return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        value, min_ = self.stack[-1]
        return min_
        # return self.thehelp[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

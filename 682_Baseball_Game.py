class Solution:
    def calPoints(self, ops: List[str]) -> int:

        queue = []

        for cur in ops:

            if cur == "+":
                queue.append(queue[-1] + queue[-2])
            elif cur == "C":
                queue.pop()
            elif cur == "D":
                queue.append(2 * queue[-1])
            else:
                queue.append(int(cur))

        return sum(queue)

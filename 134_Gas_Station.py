class Solution:

    def is_possible(self):
    # Find sum(gas) - sum(cost)
    # If negative, solution is not possible
        tank = 0

        for i in range(len(self.gas)):
            tank += self.gas[i] - self.cost[i]

        if tank < 0:
            return False
        return True

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        self.gas = gas
        self.cost = cost

        if not self.is_possible():
            return -1

        ans = 0
        tank = 0

        for i in range(len(self.gas)):
        # Guaranteed to be possible at this point, so start at where tank has < 0 fuel
            tank += self.gas[i] - self.cost[i]

            if tank < 0:
                tank = 0
                ans = i + 1

        return ans

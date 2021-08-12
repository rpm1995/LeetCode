class Solution:

    def is_possible(self, max_weight):

        total_weight = 0
        total_days = 1

        for weight in self.weights:

            if total_weight + weight > max_weight:
                total_weight = weight
                total_days += 1

            else:
                total_weight += weight

        return total_days <= self.days

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        self.weights = weights
        self.days = days
        min_possible_weight = max(weights)
        max_possible_weight = sum(weights)

        left = min_possible_weight
        right = max_possible_weight

        while left < right:

            mid = (left + right) // 2

            if self.is_possible(mid):
                right = mid

            else:
                left = mid + 1

        return left

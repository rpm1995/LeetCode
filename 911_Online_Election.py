class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        self.persons = persons
        self.times = times
        self.leaders = []
        leader = -1
        counts = {-1: -1}

        for index, person in enumerate(self.persons):

            if person not in counts:
                counts[person] = 0
            counts[person] += 1

            if counts[person] >= counts[leader]:
                leader = person

            self.leaders.append(leader)

    def binarySearch(self, t):

        left = 0
        right = len(self.times) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2
            time = self.times[mid]

            if time == t:
                return mid

            if time < t:
                ans = max(ans, mid)
                left = mid + 1

            else:
                right = mid - 1

        return ans

    def q(self, t: int) -> int:

        time = self.binarySearch(t)

        return self.leaders[time]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

class Solution:
    def countArrangement(self, N: int) -> int:

        def helper(N, count, counter, visited):

            if count > N:
                counter += 1
                # return counter

            else:

                for current in range(1, N + 1):
                    if (count % current == 0 or current % count == 0) and visited[current] is False:
                        visited[current] = True
                        counter = helper(N, count + 1, counter, visited)
                        visited[current] = False

            return counter

        return helper(N, 1, 0, [False for _ in range(N + 1)])

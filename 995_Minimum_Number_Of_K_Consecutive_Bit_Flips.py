from collections import deque


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:

        #         ans = 0

        #         for i in range(len(A)):
        #             if A[i] == 0:
        #                 if i + K - 1 >= len(A):
        #                     return - 1

        #                 ans += 1
        #                 for inner in range(K):
        #                     A[i + inner] ^= 1

        #         return ans

        queue = deque([])
        ans = 0

        for i in range(len(A)):

            if len(queue) % 2 == 0:  # Even number of flips => No flips done
                if A[i] == 0:
                    ans += 1
                    queue.append(i + K - 1)

            else:  # Odd number of flips => One flip
                if A[i] == 1:
                    ans += 1
                    queue.append(i + K - 1)

            while queue and queue[0] <= i:
                queue.popleft()

        return ans if not queue else -1

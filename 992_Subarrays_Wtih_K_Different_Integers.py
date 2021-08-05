class Solution:

    def subarrays_with_atmost_K_distinct(self, k):

        if k == 0:
            return 0

        start = 0
        end = 0
        a_dict = {}
        ans = 0

        while end < len(self.a):

            a_end = self.a[end]

            if a_end not in a_dict:
                a_dict[a_end] = 0
            a_dict[a_end] += 1

            while start < end and len(a_dict) > k:

                a_start = self.a[start]
                a_dict[a_start] -= 1

                if a_dict[a_start] == 0:
                    del a_dict[a_start]

                start += 1

            ans += end - start + 1
            end += 1

        return ans

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        self.a = A
        return self.subarrays_with_atmost_K_distinct(K) - self.subarrays_with_atmost_K_distinct(K - 1)

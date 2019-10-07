class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:

        prefix_sum = [0 for _ in range(len(A) + 1)]
        ans = 0

        for index, element in enumerate(A):
            prefix_sum[index + 1] = prefix_sum[index] + element

        for first_index, first_element in enumerate(prefix_sum):
            for second_index, second_element in enumerate(prefix_sum[first_index + 1:]):

                sub_array_sum = second_element - first_element

                if sub_array_sum % K == 0:
                    ans += 1

        return ans

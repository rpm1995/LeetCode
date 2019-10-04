class Solution:
    def knightDialer(self, N: int) -> int:

        mappings = {0: [4, 6],
                    1: [6, 8],
                    2: [9, 7],
                    3: [4, 8],
                    4: [3, 9, 0],
                    5: [],
                    6: [1, 7, 0],
                    7: [2, 6],
                    8: [1, 3],
                    9: [2, 4]}

        self.ans = 0
        numbers_seen = set()

        def helper(hops_left, current_digit, current_number):

            if hops_left == 0:
                self.ans += 1
                numbers_seen.add(current_number)

            else:
                for mapping in mappings[current_digit]:
                    helper(hops_left - 1, mapping, current_number * 10 + mapping)

        for first_digit in range(0, 10):
            helper(N - 1, first_digit, first_digit)

        return self.ans

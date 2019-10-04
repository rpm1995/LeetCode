class Solution:
    def knightDialer(self, N: int) -> int:

        #         mappings = {0: [4, 6],
        #                    1: [6, 8],
        #                    2: [9, 7],
        #                    3: [4, 8],
        #                    4: [3, 9, 0],
        #                    5: [],
        #                    6: [1, 7, 0],
        #                    7: [2, 6],
        #                    8: [1, 3],
        #                    9: [2, 4]}

        #         self.ans = 0

        #         def helper(hops_left, current_digit, current_number):

        #             if hops_left == 0:
        #                 self.ans += 1

        #             else:
        #                 for mapping in mappings[current_digit]:
        #                     helper(hops_left-1, mapping, current_number*10 + mapping)

        #         for first_digit in range(0, 10):
        #             helper(N-1, first_digit, first_digit)

        #         return self.ans

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
        cache = {}
        mod = 10 ** 9 + 7

        def helper(hops_left, current_digit, current_number, current_length):

            if (current_digit, hops_left) in cache:
                return cache[(current_digit, hops_left)]

            if hops_left == 0:
                return 1

            else:
                length = 0

                for mapping in mappings[current_digit]:
                    length += helper(hops_left - 1, mapping, current_number * 10 + mapping, current_length + 1)

                cache[(current_digit, hops_left)] = length

            # self.ans += cache[(current_digit, hops_left)]
            return cache[(current_digit, hops_left)]

        if N == 1:
            return 10

        for first_digit in range(0, 10):
            self.ans += helper(N - 1, first_digit, first_digit, 1)

        return self.ans % mod

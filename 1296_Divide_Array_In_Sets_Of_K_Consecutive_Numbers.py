class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        def getLowestNumber(frequencies):

            lowest = float('inf')

            for number, frequency in frequencies.items():

                if frequency > 0:
                    lowest = min(lowest, number)

            return lowest

        freqs = {}

        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1

        nums = set(nums)

        while nums:

            lowest_number = getLowestNumber(freqs)

            if lowest_number == float('inf'):
                return False

            count = k - 1
            freqs[lowest_number] -= 1

            if freqs[lowest_number] <= 0:
                nums.remove(lowest_number)

            while count:
                lowest_number += 1

                if lowest_number in freqs and freqs[lowest_number] > 0:

                    count -= 1
                    freqs[lowest_number] -= 1

                    if freqs[lowest_number] <= 0:
                        nums.remove(lowest_number)

                else:
                    return False

        return True

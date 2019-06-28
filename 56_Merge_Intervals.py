class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        ans = []
        intervals.sort()
        ans.append(intervals[0])

        for start, end in intervals[1:]:

            if start > ans[-1][1]:
                ans.append([start, end])

            else:
                if end > ans[-1][1]:
                    ans[-1][1] = end

        return ans

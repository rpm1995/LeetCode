import numpy


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def max_points_on_line(point):

            def calculate(point1, point2, count, duplicates, horizontal_lines):

                point1x = points[point1][0]
                point1y = points[point1][1]
                point2x = points[point2][0]
                point2y = points[point2][1]

                if point1x == point2x and point1y == point2y:
                    duplicates += 1

                elif point1x == point2x:
                    horizontal_lines += 1
                    count = max(count, horizontal_lines)

                else:
                    slope = ((point2y - point1y) * numpy.longdouble(1)) / (point2x - point1x)

                    if slope not in slopes_through_this_point:
                        slopes_through_this_point[slope] = 0
                    slopes_through_this_point[slope] += 1
                    count = max(count, slopes_through_this_point[slope])

                return count, duplicates, horizontal_lines

            slopes_through_this_point = {}
            duplicates = 0
            count = 0
            horizontal_lines = 0

            # for other_point in range(point+1, n):
            for other_point in range(n):
                count, duplicates, horizontal_lines = calculate(point, other_point, count, duplicates, horizontal_lines)

            return count + duplicates

        n = len(points)

        if n < 3:
            return n

        ans = 1

        for point in range(n):
            ans = max(ans, max_points_on_line(point))

        return ans

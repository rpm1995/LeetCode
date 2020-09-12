# class Solution:
#     def minCost(self, costs: List[List[int]]) -> int:
#
#         def find_cost(house, cur_color):
#
#             if house == n:
#                 return 0
#
#             child_cost = float('inf')
#
#             for next_color in range(3):
#
#                 if next_color != cur_color:
#                     child_cost = min(child_cost, find_cost(house + 1, next_color))
#
#             total_cost = child_cost + costs[house][cur_color]
#             return total_cost
#
#         n = len(costs)
#         ans = min(find_cost(0, 0), find_cost(0, 1), find_cost(0, 2))
#         return ans

# class Solution:
#     def minCost(self, costs: List[List[int]]) -> int:
#
#         def find_cost(house, cur_color, visited):
#
#             if house == n:
#                 return 0
#
#             if (house, cur_color) in visited:
#                 return visited[(house, cur_color)]
#
#             child_cost = float('inf')
#
#             for next_color in range(3):
#
#                 if next_color != cur_color:
#                     child_cost = min(child_cost, find_cost(house + 1, next_color, visited))
#
#             total_cost = child_cost + costs[house][cur_color]
#             visited[(house, cur_color)] = total_cost
#
#             return visited[(house, cur_color)]
#
#         n = len(costs)
#         ans = min(find_cost(0, 0, {}), find_cost(0, 1, {}), find_cost(0, 2, {}))
#         return ans

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        n = len(costs)

        if n == 0:
            return 0

        for i in range(n - 2, -1, -1):
            costs[i][0] += min(costs[i + 1][1], costs[i + 1][2])
            costs[i][1] += min(costs[i + 1][0], costs[i + 1][2])
            costs[i][2] += min(costs[i + 1][0], costs[i + 1][1])

        return min(costs[0])

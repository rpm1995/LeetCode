class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:

        def dfs(cur, manager):

            time_so_far = informTime[cur]
            time_for_subs = 0

            if cur in manager:
                for employee in manager[cur]:
                    time_for_subs = max(time_for_subs, dfs(employee, manager))

            return time_so_far + time_for_subs

        manager = {}
        ans = 0

        for employee, man in enumerate(managers):

            if man not in manager:
                manager[man] = []
            manager[man].append(employee)

        ans = dfs(headID, manager)

        return ans

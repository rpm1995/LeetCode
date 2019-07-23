class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        if not M:
            return 0

        visited = [0 for _ in range(len(M))]
        circles = 0
        adj_list = {}
        n = len(M)


        def dfs(friend):

            visited[friend] = 1

            for friends in adj_list[friend]:
                if visited[friends] == 0:
                    dfs(friends)

            return


        for friend1 in range(n):
            for friend2 in range(n):

                if M[friend1][friend2] == 1:
                    if friend1 not in adj_list:
                        adj_list[friend1] = []
                    if friend2 not in adj_list:
                        adj_list[friend2] = []

                    adj_list[friend1].append(friend2)
                    adj_list[friend2].append(friend1)

        for index, friend in enumerate(visited):
            if friend == 0:
                dfs(index)
                circles += 1


        return circles

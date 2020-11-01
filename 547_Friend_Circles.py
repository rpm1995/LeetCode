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


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        class unionFind:

            def __init__(self, n):

                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [0 for _ in range(n)]

            def find(self, x):

                if self.parent[x] == x:
                    return x

                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):

                x_node = self.find(self.parent[x])
                y_node = self.find(self.parent[y])

                if x_node != y_node:

                    if self.rank[x_node] < self.rank[y_node]:
                        self.parent[x_node] = y_node

                    else:
                        self.parent[y_node] = x_node

                        if self.rank[x_node] == self.rank[y_node]:
                            self.rank[x_node] += 1

                    self.count -= 1
                return

            def get_count(self):

                return self.count

        n = len(M)
        union_tree = unionFind(n)

        for friend1 in range(n):
            for friend2 in range(friend1 + 1, n):

                if friend1 != friend2 and M[friend1][friend2] == 1:
                    union_tree.union(friend1, friend2)

        return union_tree.get_count()


######################## Commented Approach works!

class UnionFind:

    def __init__(self, size):

        self.parents = [i for i in range(size)]
        self.components = size
        self.component_size = {i: 1 for i in range(size)}

    def find(self, node):

        if self.parents[node] == node:
            return node

        self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def getComponents(self):

        return self.components

    def union(self, node1, node2):

        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return

        if self.component_size[root1] > self.component_size[root2]:
            self.parents[root2] = root1
            self.component_size[root2] += self.component_size[root1]

        else:
            self.parents[root1] = root2
            self.component_size[root1] += self.component_size[root2]

        self.components -= 1

    # def cleanUp(self):
    #
    #     for kids in self.parents:
    #         temp = self.find(kids)


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        n = len(M)
        disjoint_set = UnionFind(n)
        # ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    disjoint_set.union(i, j)

        # disjoint_set.cleanUp()
        #
        # for index, kids in enumerate(disjoint_set.parents):
        #     if index == kids:
        #         ans += 1
        #
        # return ans

        return disjoint_set.components


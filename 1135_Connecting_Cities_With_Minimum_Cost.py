class UnionFind:

    def __init__(self, n):

        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]
        self.components = n

    def find(self, node):

        if self.parent[node] == node:
            return node

        self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, x, y):

        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return

        rank_x = self.rank[parent_x]
        rank_y = self.rank[parent_y]

        if rank_x < rank_y:
            self.parent[parent_x] = parent_y

        else:
            self.parent[parent_y] = parent_x

            if rank_x == rank_y:
                self.rank[parent_x] += 1

        self.components -= 1

        return

    def getComponents(self):

        return self.components


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:

        ans = 0
        connections.sort(key=lambda x: x[2])
        disjoint_set = UnionFind(n)

        for edge1, edge2, cost in connections:

            parent1 = disjoint_set.find(edge1)
            parent2 = disjoint_set.find(edge2)

            if parent1 != parent2:
                disjoint_set.union(edge1, edge2)
                ans += cost

            if disjoint_set.getComponents() == 1:
                return ans

        return -1

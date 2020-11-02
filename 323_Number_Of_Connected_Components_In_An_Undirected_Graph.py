class UnionFind:

    def __init__(self, n):

        self.parents = [i for i in range(n)]
        self.size = {i: 1 for i in range(n)}
        self.components = n

    def find(self, node):

        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def union(self, node1, node2):

        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:

            if self.size[root1] > self.size[root2]:
                self.parents[root2] = root1
                self.size[root1] += self.size[root2]

            else:
                self.parents[root1] = root2
                self.size[root2] += self.size[root1]

            self.components -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjoint_set = UnionFind(n)

        for node1, node2 in edges:
            disjoint_set.union(node1, node2)

        return disjoint_set.components

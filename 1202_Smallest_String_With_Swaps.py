class UnionFind:

    def __init__(self, n):

        self.parents = list(range(n))
        self.size = {i: 1 for i in range(n)}

    def find(self, node):

        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def union(self, node_1, node_2):

        root_1 = self.find(node_1)
        root_2 = self.find(node_2)

        if root_1 != root_2:

            if self.size[root_1] > self.size[root_2]:
                self.parents[root_2] = root_1
                self.size[root_1] += self.size[root_2]

            else:
                self.parents[root_1] = root_2
                self.size[root_2] += self.size[root_1]


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        # All connected indices can move characters between each other

        n = len(s)
        disjoint_set = UnionFind(n)
        components = {}
        ans = ''

        for index1, index2 in pairs:
            disjoint_set.union(index1, index2)

        for index, character in enumerate(s):
            component = disjoint_set.find(index)

            if component not in components:
                components[component] = []
            components[component].append(character)

        for array in components.values():
            array.sort(reverse=True)

        for index in range(n):
            character = components[disjoint_set.find(index)].pop()
            ans += character

        return ans

class Solution:

    def buildGraph(self, connections, n):

        for node1, node2 in connections:

            if node1 not in self.graph:
                self.graph[node1] = []
            if node2 not in self.graph:
                self.graph[node2] = []

            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

            self.edges.add((min(node1, node2), max(node1, node2)))

        return

    def dfs(self, node, discovery_rank):

        if self.ranks[node]:
            return self.ranks[node]

        self.ranks[node] = discovery_rank

        global_min_rank = discovery_rank + 1

        for neighbour in self.graph[node]:

            if self.ranks[neighbour] and self.ranks[neighbour] == (discovery_rank - 1):
                continue

            local_min_rank = self.dfs(neighbour, discovery_rank + 1)

            if local_min_rank <= discovery_rank:
                if (min(node, neighbour), max(node, neighbour)) in self.edges:
                    self.edges.remove((min(node, neighbour), max(node, neighbour)))

            global_min_rank = min(global_min_rank, local_min_rank)

        return global_min_rank

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        self.edges = set()
        self.ranks = {i: None for i in range(n)}
        self.graph = {}

        self.buildGraph(connections, n)

        ans = []
        self.dfs(0, 0)

        for node1, node2 in self.edges:
            ans.append([node1, node2])

        return ans

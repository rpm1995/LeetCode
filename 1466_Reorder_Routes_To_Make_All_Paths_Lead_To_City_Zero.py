class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        visited = set()
        connection = {}
        inverse = {}
        self.ans = 0

        def dfs(node):

            visited.add(node)

            if node in connection:
                for neighbour in connection[node]:
                    if neighbour not in visited:
                        self.ans += 1
                        dfs(neighbour)

            if node in inverse:
                for neighbour in inverse[node]:
                    if neighbour not in visited:
                        dfs(neighbour)

        for node1, node2 in connections:

            if node1 not in connection:
                connection[node1] = []
            connection[node1].append(node2)

            if node2 not in inverse:
                inverse[node2] = []
            inverse[node2].append(node1)

        dfs(0)
        return self.ans

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj_list = {}

        def dfs(cur, target):

            if cur == target:
                return True

            if cur not in visited:
                visited.add(cur)

            for neighbour in adj_list[cur]:
                if neighbour not in visited and dfs(neighbour, target) is True:
                    return True

            return False

        for node1, node2 in edges:

            visited = set()

            if node1 in adj_list and node2 in adj_list and dfs(node1, node2):
                return node1, node2

            if node1 not in adj_list:
                adj_list[node1] = set()
            adj_list[node1].add(node2)

            if node2 not in adj_list:
                adj_list[node2] = set()
            adj_list[node2].add(node1)

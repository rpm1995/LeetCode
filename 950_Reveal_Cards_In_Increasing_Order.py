class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        #         adj_list = {}

        #         def dfs(cur, target):

        #             if cur == target:
        #                 return True

        #             if cur not in visited:
        #                 visited.add(cur)

        #             for neighbour in adj_list[cur]:
        #                 if neighbour not in visited and dfs(neighbour, target) is True:
        #                     return True

        #             return False

        #         for node1, node2 in edges:

        #             visited = set()

        #             if node1 in adj_list and node2 in adj_list and dfs(node1, node2):
        #                 return node1, node2

        #             if node1 not in adj_list:
        #                 adj_list[node1] = set()
        #             adj_list[node1].add(node2)

        #             if node2 not in adj_list:
        #                 adj_list[node2] = set()
        #             adj_list[node2].add(node1)

        def find(node):

            if parent[node] == 0:
                return node

            parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):

            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return False

            parent[root1] = root2
            return True

        parent = [0 for _ in range(len(edges))]

        for node1, node2 in edges:

            if not union(node1 - 1, node2 - 1):
                return node1, node2

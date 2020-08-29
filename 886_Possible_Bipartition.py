class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        if not dislikes:
            return True

        adj_list = {}
        color = [-1 for _ in range(N + 1)]

        for node1, node2 in dislikes:

            if node1 not in adj_list:
                adj_list[node1] = []

            if node2 not in adj_list:
                adj_list[node2] = []

            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        for node in range(1, N + 1):

            if color[node] == -1 and node in adj_list:
                stack = [node]
                color[node] = 0

                while stack:
                    cur_node = stack.pop()
                    cur_color = color[cur_node]

                    for neighbour in adj_list[cur_node]:

                        if color[neighbour] == -1:
                            color[neighbour] = cur_color ^ 1
                            stack.append(neighbour)

                        elif color[neighbour] == cur_color:
                            return False

        return True

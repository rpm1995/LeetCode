class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color = [-1 for _ in range(len(graph))]

        for node in range(len(graph)):

            if color[node] == -1:
                stack = [node]
                color[node] = 0

                while stack:
                    cur_node = stack.pop()
                    cur_color = color[cur_node]

                    for neighbour in graph[cur_node]:

                        if color[neighbour] == -1:
                            color[neighbour] = cur_color ^ 1
                            stack.append(neighbour)

                        elif color[neighbour] == cur_color:
                            return False

        return True

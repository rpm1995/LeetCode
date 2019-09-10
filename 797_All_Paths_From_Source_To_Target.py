class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        adjlist = {}
        start = 0
        end = len(graph) - 1
        ans = []

        for index, nodes in enumerate(graph):
            adjlist[index] = nodes

        def dfs(current, res):

            if current == end:
                ans.append(res[:])

            else:
                for neighbour in adjlist[current]:
                    res.append(neighbour)
                    dfs(neighbour, res)
                    res.pop()

        dfs(start, [0])
        return ans

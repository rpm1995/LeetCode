from collections import deque

# First do a BFS, record the minimum number of steps it takes to reach every word (and the final word)
# Then do a DFS, exploring each branch only if the steps it takes to reach that branch is the same as the
# recorded number of steps


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def dfs(curword):

            res.append(curword)

            if curword == endWord:
                ans.append(res[:])
                res.pop()
                return

            if curword in adjlist:
                for neighbour in adjlist[curword]:
                    if min_distance[neighbour] == min_distance[curword] + 1:
                        dfs(neighbour)

            res.pop()
            return

        wordList = set(wordList)
        queue = deque([])
        adjlist = {}
        min_distance = {}
        visited = set()
        alphabets = "abcdefghijklmnopqrstuvwxyz"

        queue.append((beginWord, 0))
        visited.add(beginWord)

        while queue:

            curword, distance = queue.popleft()

            min_distance[curword] = distance

            for index, char in enumerate(curword):
                for alpha in alphabets:
                    if alpha != char:
                        newWord = curword[: index] + alpha + curword[index + 1:]

                        if newWord in wordList:
                            if newWord not in adjlist:
                                adjlist[newWord] = set()
                            adjlist[newWord].add(curword)

                            if curword not in adjlist:
                                adjlist[curword] = set()
                            adjlist[curword].add(newWord)

                            if newWord not in visited:
                                visited.add(newWord)
                                queue.append((newWord, distance + 1))

        if endWord not in adjlist:
            return []

        # print(min_distance)
        # print(adjlist)

        ans = []
        res = []
        dfs(beginWord)
        return ans

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(course1, course2):

            if visited[course1] == 2:
                return False

            # if course1 == course2:
            #     visited[course1] = 1
            #     return True

            if visited[course1] == 1:
                return True

            visited[course1] = 2

            for prereq in prereqs[course1]:
                if dfs(prereq, course2) is False:
                    return False

            visited[course1] = 1
            return True

        prereqs = {}
        visited = [0 for _ in range(numCourses)]

        for course in range(numCourses):
            prereqs[course] = []

        for course1, course2 in prerequisites:
            prereqs[course1].append(course2)

        for course1, course2 in prerequisites:

            if visited[course1] == 0:
                if dfs(course1, course2) is False:
                    return False

        return True

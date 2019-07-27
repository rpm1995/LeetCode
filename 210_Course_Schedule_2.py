class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        def dfs(course):

            if courses[course] == 1:
                return False

            if courses[course] == 2:
                return True

            courses[course] = 1

            if course in prereqs:
                for prereq in prereqs[course]:
                    if dfs(prereq) is False:
                        return False

            ans.append(course)
            courses[course] = 2
            # print(ans)

            return True

        prereqs = {}
        courses = [0 for _ in range(numCourses)]
        ans = []

        for course, prereq in prerequisites:

            if course not in prereqs:
                prereqs[course] = []
            prereqs[course].append(prereq)

        #         Can't do it this way because of silly test cases
        #         for course, prereq in prerequisites:
        #             if dfs(course) is False:
        #                 return []

        #         return ans

        for index, course in enumerate(courses):
            if dfs(index) is False:
                return []

        return ans

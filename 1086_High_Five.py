class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """

        students = {}
        ans = []

        for student, score in items:
            if student not in students:
                students[student] = []
            students[student].append(score)

        for ids, scores in students.items():
            scores.sort(reverse=True)
            average = int(sum(scores[:5]) / 5)
            students[ids] = average

        for ids in range(1, 1000):                  # Given constraint
            if ids in students:
                ans.append([ids, students[ids]])

        return ans

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def isMatch(s1_dict, s2_dict):

            for key, value in s2_dict.items():

                if key not in s1_dict or s1_dict[key] != value:
                    return False

            return len(s1_dict) == len(s2_dict)

        s1_dict = {}
        s2_dict = {}
        s1_counts = len(s1)
        s2_counts = 0
        left = 0

        for char in s1:

            if char not in s1_dict:
                s1_dict[char] = 0
            s1_dict[char] += 1

        for right, char in enumerate(s2):

            if char in s1_dict:

                if char not in s2_dict:
                    s2_dict[char] = 0
                s2_dict[char] += 1

            while right - left + 1 > s1_counts:

                if s2[left] in s2_dict:

                    if s2_dict[s2[left]] == 1:
                        del s2_dict[s2[left]]
                    else:
                        s2_dict[s2[left]] -= 1

                left += 1

            if isMatch(s1_dict, s2_dict):
                return True

        return False

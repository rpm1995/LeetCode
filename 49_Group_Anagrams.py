class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = []
        one_hot = {}

        for word in strs:
            mapping = [0 for _ in range(26)]

            for char in word:
                representation = ord(char)
                mapping[representation % 26] += 1

            mapping = tuple(mapping)

            if mapping not in one_hot:
                one_hot[mapping] = []
            one_hot[mapping].append(word)

        for key, values in one_hot.items():
            ans.append(values)

        return ans
